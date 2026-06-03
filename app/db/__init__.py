from app.db.base import Base
from app.db.models import (
    AboutUsPage,
    ContactUsPage,
    CoursesPage,
    DestinationsPage,
    FooterPage,
    HomePage,
    StudyAbroadPage,
)

__all__ = [
    "Base",
    "HomePage",
    "CoursesPage",
    "DestinationsPage",
    "StudyAbroadPage",
    "AboutUsPage",
    "ContactUsPage",
    "FooterPage",
]
