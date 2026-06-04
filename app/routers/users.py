from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.auth import get_current_admin_user
from app.db.deps import get_db
from app.db.models import AdminUser, ROLE_SUPERADMIN, ROLE_USER
from app.passwords import hash_password
from app.schemas import AdminUserCreate, AdminUserResponse, AdminUserUpdate

router = APIRouter(prefix="/api/users", tags=["users"])


def _to_response(row: AdminUser) -> AdminUserResponse:
    return AdminUserResponse(
        id=row.id,
        email=row.email,
        name=row.name,
        role=row.role,
        created_at=row.created_at,
    )


@router.get("", response_model=list[AdminUserResponse])
def list_users(
    db: Session = Depends(get_db),
    _: AdminUser = Depends(get_current_admin_user),
) -> list[AdminUserResponse]:
    rows = db.query(AdminUser).order_by(AdminUser.created_at.asc()).all()
    return [_to_response(r) for r in rows]


@router.post("", response_model=AdminUserResponse, status_code=status.HTTP_201_CREATED)
def create_user(
    body: AdminUserCreate,
    db: Session = Depends(get_db),
    _: AdminUser = Depends(get_current_admin_user),
) -> AdminUserResponse:
    email = body.email.strip().lower()
    if not email or "@" not in email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid email address")
    if len(body.password) < 6:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password must be at least 6 characters",
        )

    row = AdminUser(
        email=email,
        password_hash=hash_password(body.password),
        name=body.name.strip(),
        role=ROLE_USER,
    )
    db.add(row)
    try:
        db.commit()
        db.refresh(row)
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A user with this email already exists",
        ) from exc

    return _to_response(row)


@router.put("/{user_id}", response_model=AdminUserResponse)
def update_user(
    user_id: int,
    body: AdminUserUpdate,
    db: Session = Depends(get_db),
    _: AdminUser = Depends(get_current_admin_user),
) -> AdminUserResponse:
    email = body.email.strip().lower()
    if not email or "@" not in email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid email address")

    row = db.query(AdminUser).filter(AdminUser.id == user_id).first()
    if row is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    if body.password is not None and body.password != "":
        if len(body.password) < 6:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Password must be at least 6 characters",
            )
        row.password_hash = hash_password(body.password)

    row.email = email
    row.name = body.name.strip()

    try:
        db.commit()
        db.refresh(row)
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A user with this email already exists",
        ) from exc

    return _to_response(row)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current: AdminUser = Depends(get_current_admin_user),
) -> None:
    if current.id == user_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="You cannot delete your own account")

    row = db.query(AdminUser).filter(AdminUser.id == user_id).first()
    if row is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    if row.role == ROLE_SUPERADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The primary administrator account cannot be deleted",
        )

    db.delete(row)
    db.commit()
