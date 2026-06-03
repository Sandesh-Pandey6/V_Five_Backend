from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile, status

from app.auth import get_current_admin_user
from app.config import settings
from app.db.models import AdminUser
from app.schemas import UploadResponse, UploadStatusResponse
from app.services.cloudinary_service import upload_image

router = APIRouter(prefix="/api/uploads", tags=["uploads"])


@router.get("/status", response_model=UploadStatusResponse)
def upload_status() -> UploadStatusResponse:
    return UploadStatusResponse(
        configured=settings.cloudinary_configured,
        max_upload_mb=settings.max_upload_mb,
    )


@router.post("/image", response_model=UploadResponse)
async def upload_image_endpoint(
    file: UploadFile = File(...),
    folder: str = Form("cms"),
    _: AdminUser = Depends(get_current_admin_user),
) -> UploadResponse:
    if not file.content_type:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Could not determine file type",
        )

    file_bytes = await file.read()
    if not file_bytes:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Empty file")

    parts = [
        "".join(c for c in part if c.isalnum() or c in "-_") or "misc"
        for part in folder.split("/")
        if part.strip()
    ]
    safe_folder = "/".join(parts) if parts else "cms"
    result = upload_image(file_bytes, folder=safe_folder, content_type=file.content_type)
    return UploadResponse(**result)
