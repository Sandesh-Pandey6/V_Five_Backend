from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.auth import authenticate_user, create_access_token, get_current_admin_user
from app.db.deps import get_db
from app.db.models import AdminUser
from app.passwords import hash_password
from app.schemas import AdminMeResponse, AdminUserCreate, AdminUserResponse, LoginRequest, LoginResponse

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/login", response_model=LoginResponse)
def login(body: LoginRequest, db: Session = Depends(get_db)) -> LoginResponse:
    email = body.email.strip().lower()
    if not email or "@" not in email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid email address")

    user = authenticate_user(db, email, body.password)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )
    token = create_access_token(user.id)
    return LoginResponse(access_token=token)


@router.get("/me", response_model=AdminMeResponse)
def me(user: AdminUser = Depends(get_current_admin_user)) -> AdminMeResponse:
    return AdminMeResponse(id=user.id, email=user.email, name=user.name, role=user.role)
