from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth import get_current_admin_user
from app.db.deps import get_db
from app.db.models import AdminUser, Inquiry
from app.schemas import InquiryCreate, InquiryResponse, InquirySubmitResponse

router = APIRouter(prefix="/api/inquiries", tags=["inquiries"])


@router.post("", response_model=InquirySubmitResponse)
def submit_inquiry(body: InquiryCreate, db: Session = Depends(get_db)) -> InquirySubmitResponse:
    row = Inquiry(
        name=body.name.strip(),
        phone=body.phone.strip(),
        email=body.email.strip(),
        course=body.course.strip(),
        message=body.message.strip(),
    )
    db.add(row)
    db.commit()
    return InquirySubmitResponse()


@router.get("", response_model=list[InquiryResponse])
def list_inquiries(
    db: Session = Depends(get_db),
    _: AdminUser = Depends(get_current_admin_user),
) -> list[InquiryResponse]:
    rows = db.query(Inquiry).order_by(Inquiry.created_at.desc()).limit(200).all()
    return [
        InquiryResponse(
            id=r.id,
            name=r.name,
            phone=r.phone,
            email=r.email,
            course=r.course,
            message=r.message,
            created_at=r.created_at,
        )
        for r in rows
    ]


@router.delete("/{inquiry_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_inquiry(
    inquiry_id: int,
    db: Session = Depends(get_db),
    _: AdminUser = Depends(get_current_admin_user),
) -> None:
    row = db.query(Inquiry).filter(Inquiry.id == inquiry_id).first()
    if row is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Inquiry not found")
    db.delete(row)
    db.commit()
