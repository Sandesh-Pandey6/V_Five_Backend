"""Seed CMS sections from defaults (or legacy JSON). Run after: alembic upgrade head"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.db.session import SessionLocal
from app.repositories.cms_repository import cms_repository


def main() -> None:
    db = SessionLocal()
    try:
        for key in ("home", "courses", "destinations", "studyAbroad", "about", "contact"):
            cms_repository.get_section(db, key)
            print(f"Seeded section: {key}")
    finally:
        db.close()
    print("Done.")


if __name__ == "__main__":
    main()
