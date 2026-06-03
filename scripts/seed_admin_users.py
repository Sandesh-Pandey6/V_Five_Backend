"""Create the default admin user if the admin_users table is empty."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.config import settings
from app.db.models import AdminUser, ROLE_SUPERADMIN
from app.db.session import SessionLocal
from app.passwords import hash_password


def main() -> None:
    db = SessionLocal()
    try:
        existing = db.query(AdminUser).count()
        if existing > 0:
            print(f"Admin users already exist ({existing} user(s)). Skipping seed.")
            return

        email = settings.admin_email.strip().lower()
        user = AdminUser(
            email=email,
            password_hash=hash_password(settings.admin_password),
            name="Administrator",
            role=ROLE_SUPERADMIN,
        )
        db.add(user)
        db.commit()
        print(f"Created default admin user: {email}")
    finally:
        db.close()


if __name__ == "__main__":
    main()
