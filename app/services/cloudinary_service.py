import cloudinary
import cloudinary.uploader
from fastapi import HTTPException, status

from app.config import settings

ALLOWED_CONTENT_TYPES = {
    "image/jpeg",
    "image/png",
    "image/webp",
    "image/gif",
}


def _ensure_configured() -> None:
    if not settings.cloudinary_configured:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=(
                "Cloudinary is not configured. Set CLOUDINARY_CLOUD_NAME, "
                "CLOUDINARY_API_KEY, and CLOUDINARY_API_SECRET in backend/.env"
            ),
        )


def _init_cloudinary() -> None:
    cloudinary.config(
        cloud_name=settings.cloudinary_cloud_name,
        api_key=settings.cloudinary_api_key,
        api_secret=settings.cloudinary_api_secret,
        secure=True,
    )


def upload_image(file_bytes: bytes, *, folder: str, content_type: str) -> dict[str, str]:
    _ensure_configured()

    if content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only JPEG, PNG, WebP, and GIF images are allowed",
        )

    max_bytes = settings.max_upload_mb * 1024 * 1024
    if len(file_bytes) > max_bytes:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Image must be smaller than {settings.max_upload_mb} MB",
        )

    _init_cloudinary()
    upload_folder = f"{settings.cloudinary_folder}/{folder}".strip("/")

    try:
        result = cloudinary.uploader.upload(
            file_bytes,
            folder=upload_folder,
            resource_type="image",
            overwrite=True,
        )
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"Cloudinary upload failed: {exc}",
        ) from exc

    return {
        "url": result["secure_url"],
        "public_id": result["public_id"],
    }
