"""Test PostgreSQL connection using DATABASE_URL from backend/.env"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import create_engine, inspect, text

from app.config import settings

NAVBAR_TABLES = (
    "home",
    "courses",
    "destinations",
    "study_abroad",
    "about_us",
    "contact_us",
    "footer",
)


def main() -> None:
    print(f"Connecting to: {settings.database_url.split('@')[-1]}")
    try:
        engine = create_engine(settings.database_url)
        with engine.connect() as conn:
            version = conn.execute(text("SELECT version()")).scalar()
            print("Database connection successful!")
            print(f"PostgreSQL: {str(version)[:60]}...")

            tables = set(inspect(engine).get_table_names())
            missing = [t for t in NAVBAR_TABLES if t not in tables]
            if missing:
                print(f"Missing tables: {', '.join(missing)}")
                print("Run: alembic upgrade head")
            else:
                print("Admin navbar tables found:")
                for name in NAVBAR_TABLES:
                    count = conn.execute(text(f'SELECT COUNT(*) FROM "{name}"')).scalar()
                    print(f"  - {name}: {count} row(s)")
    except Exception as exc:
        print("Connection FAILED:")
        print(f"  {exc}")
        print("\nSee DATABASE_SETUP.md for pgAdmin steps.")
        sys.exit(1)


if __name__ == "__main__":
    main()
