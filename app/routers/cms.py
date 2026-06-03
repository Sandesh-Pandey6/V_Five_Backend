from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth import get_current_admin_user
from app.db.deps import get_db
from app.db.models import AdminUser
from app.repositories.cms_repository import cms_repository
from app.schemas import (
    AboutUsCMSData,
    ContactCMSData,
    CoursesCMSData,
    DestinationsCMSData,
    FooterCMSData,
    HomeCMSData,
    StudyAbroadCMSData,
)

router = APIRouter(prefix="/api/cms", tags=["cms"])


@router.get("/home", response_model=HomeCMSData)
def get_home(db: Session = Depends(get_db)) -> HomeCMSData:
    return HomeCMSData.model_validate(cms_repository.get_section(db, "home"))


@router.put("/home", response_model=HomeCMSData)
def update_home(
    data: HomeCMSData,
    db: Session = Depends(get_db),
    _: AdminUser = Depends(get_current_admin_user),
) -> HomeCMSData:
    cms_repository.update_section(db, "home", data.model_dump())
    return data


@router.get("/courses", response_model=CoursesCMSData)
def get_courses(db: Session = Depends(get_db)) -> CoursesCMSData:
    return CoursesCMSData.model_validate(cms_repository.get_section(db, "courses"))


@router.put("/courses", response_model=CoursesCMSData)
def update_courses(
    data: CoursesCMSData,
    db: Session = Depends(get_db),
    _: AdminUser = Depends(get_current_admin_user),
) -> CoursesCMSData:
    cms_repository.update_section(db, "courses", data.model_dump())
    return data


@router.get("/destinations", response_model=DestinationsCMSData)
def get_destinations(db: Session = Depends(get_db)) -> DestinationsCMSData:
    return DestinationsCMSData.model_validate(cms_repository.get_section(db, "destinations"))


@router.put("/destinations", response_model=DestinationsCMSData)
def update_destinations(
    data: DestinationsCMSData,
    db: Session = Depends(get_db),
    _: AdminUser = Depends(get_current_admin_user),
) -> DestinationsCMSData:
    cms_repository.update_section(db, "destinations", data.model_dump())
    return data


@router.get("/study-abroad", response_model=StudyAbroadCMSData)
def get_study_abroad(db: Session = Depends(get_db)) -> StudyAbroadCMSData:
    return StudyAbroadCMSData.model_validate(cms_repository.get_section(db, "studyAbroad"))


@router.put("/study-abroad", response_model=StudyAbroadCMSData)
def update_study_abroad(
    data: StudyAbroadCMSData,
    db: Session = Depends(get_db),
    _: AdminUser = Depends(get_current_admin_user),
) -> StudyAbroadCMSData:
    cms_repository.update_section(db, "studyAbroad", data.model_dump())
    return data


@router.get("/about", response_model=AboutUsCMSData)
def get_about(db: Session = Depends(get_db)) -> AboutUsCMSData:
    return AboutUsCMSData.model_validate(cms_repository.get_section(db, "about"))


@router.put("/about", response_model=AboutUsCMSData)
def update_about(
    data: AboutUsCMSData,
    db: Session = Depends(get_db),
    _: AdminUser = Depends(get_current_admin_user),
) -> AboutUsCMSData:
    cms_repository.update_section(db, "about", data.model_dump())
    return data


@router.get("/contact", response_model=ContactCMSData)
def get_contact(db: Session = Depends(get_db)) -> ContactCMSData:
    return ContactCMSData.model_validate(cms_repository.get_section(db, "contact"))


@router.put("/contact", response_model=ContactCMSData)
def update_contact(
    data: ContactCMSData,
    db: Session = Depends(get_db),
    _: AdminUser = Depends(get_current_admin_user),
) -> ContactCMSData:
    cms_repository.update_section(db, "contact", data.model_dump())
    return data


@router.get("/footer", response_model=FooterCMSData)
def get_footer(db: Session = Depends(get_db)) -> FooterCMSData:
    return FooterCMSData.model_validate(cms_repository.get_section(db, "footer"))


@router.put("/footer", response_model=FooterCMSData)
def update_footer(
    data: FooterCMSData,
    db: Session = Depends(get_db),
    _: AdminUser = Depends(get_current_admin_user),
) -> FooterCMSData:
    cms_repository.update_section(db, "footer", data.model_dump())
    return data

