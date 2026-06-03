import json
from pathlib import Path
from typing import Any

from sqlalchemy import inspect, text
from sqlalchemy.orm import Session

from app.config import settings
from app.db.models import (
    AboutUsPage,
    ContactUsPage,
    CoursesPage,
    DestinationsPage,
    FooterPage,
    HomePage,
    StudyAbroadPage,
)
from app.defaults import default_store

# Internal API keys → database table (matches admin navbar)
SECTION_TABLES: dict[str, Any] = {
    "home": HomePage,
    "courses": CoursesPage,
    "destinations": DestinationsPage,
    "studyAbroad": StudyAbroadPage,
    "about": AboutUsPage,
    "contact": ContactUsPage,
    "footer": FooterPage,
}

SECTION_KEYS = tuple(SECTION_TABLES.keys())


class CMSRepository:
    def get_section(self, db: Session, key: str) -> dict:
        if key not in SECTION_TABLES:
            raise KeyError(f"Unknown CMS section: {key}")

        self._ensure_seeded(db)

        model = SECTION_TABLES[key]
        row = db.query(model).order_by(model.id).first()
        if row is not None:
            return dict(row.data)

        payload = default_store()[key]
        self.update_section(db, key, payload)
        return payload

    def update_section(self, db: Session, key: str, payload: dict) -> dict:
        if key not in SECTION_TABLES:
            raise KeyError(f"Unknown CMS section: {key}")

        model = SECTION_TABLES[key]
        row = db.query(model).order_by(model.id).first()
        if row is None:
            row = model(data=payload)
            db.add(row)
        else:
            row.data = payload

        db.commit()
        db.refresh(row)
        return dict(row.data)

    def _ensure_seeded(self, db: Session) -> None:
        if any(db.query(model).count() > 0 for model in SECTION_TABLES.values()):
            return

        legacy = self._load_legacy_json()
        legacy_sections = self._load_legacy_cms_sections(db)
        defaults = default_store()

        for key, model in SECTION_TABLES.items():
            if legacy_sections and key in legacy_sections:
                payload = legacy_sections[key]
            elif legacy and key in legacy:
                payload = legacy[key]
            else:
                payload = defaults[key]
            db.add(model(data=payload))

        db.commit()

    def _load_legacy_json(self) -> dict | None:
        path = Path(__file__).resolve().parent.parent.parent / settings.legacy_data_file
        if not path.exists():
            return None
        with path.open(encoding="utf-8") as f:
            return json.load(f)

    def _load_legacy_cms_sections(self, db: Session) -> dict | None:
        if "cms_sections" not in inspect(db.get_bind()).get_table_names():
            return None
        rows = db.execute(text("SELECT key, data FROM cms_sections")).fetchall()
        if not rows:
            return None
        return {row[0]: row[1] for row in rows}


cms_repository = CMSRepository()
