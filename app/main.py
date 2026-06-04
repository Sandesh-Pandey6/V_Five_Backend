from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.config import settings
from app.db.session import engine
from app.routers import auth, cms, inquiries, uploads, users
from app.schemas import HealthResponse

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_app: FastAPI):
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT to_regclass('public.home')"))
        logger.info("Database connection OK")
    except Exception:
        logger.warning(
            "Database unavailable or not migrated. "
            "Start Postgres and run: alembic upgrade head"
        )
    yield


app = FastAPI(
    title="V Five Education API",
    description="Backend API for V Five Education Consultancy CMS",
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_origin_regex=settings.cors_origin_regex_pattern,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(cms.router)
app.include_router(uploads.router)
app.include_router(inquiries.router)


@app.get("/api/health", response_model=HealthResponse)
def health() -> HealthResponse:
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return HealthResponse(database="connected")
    except Exception:
        return HealthResponse(status="degraded", database="disconnected")
