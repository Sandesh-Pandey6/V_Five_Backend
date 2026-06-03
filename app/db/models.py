from datetime import datetime

from sqlalchemy import DateTime, String, Text, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class _CMSPageMixin:
    """One row per table — names match the admin sidebar in pgAdmin."""

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    data: Mapped[dict] = mapped_column(JSONB, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )


class HomePage(_CMSPageMixin, Base):
    __tablename__ = "home"


class CoursesPage(_CMSPageMixin, Base):
    __tablename__ = "courses"


class DestinationsPage(_CMSPageMixin, Base):
    __tablename__ = "destinations"


class StudyAbroadPage(_CMSPageMixin, Base):
    __tablename__ = "study_abroad"


class AboutUsPage(_CMSPageMixin, Base):
    __tablename__ = "about_us"


class ContactUsPage(_CMSPageMixin, Base):
    __tablename__ = "contact_us"


class FooterPage(_CMSPageMixin, Base):
    __tablename__ = "footer"


class Inquiry(Base):
    __tablename__ = "inquiries"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    phone: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(200), nullable=False)
    course: Mapped[str] = mapped_column(String(200), nullable=False)
    message: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

ROLE_SUPERADMIN = "superadmin"
ROLE_USER = "user"


class AdminUser(Base):
    __tablename__ = "admin_users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    name: Mapped[str] = mapped_column(String(200), nullable=False, server_default="")
    role: Mapped[str] = mapped_column(
        String(32), nullable=False, server_default=ROLE_USER
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    @property
    def is_superadmin(self) -> bool:
        return self.role == ROLE_SUPERADMIN
