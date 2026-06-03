from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    admin_username: str = "admin"
    admin_password: str = "admin123"
    admin_email: str = "admin@vfiveeducation.com"
    secret_key: str = "vfive-dev-secret-change-in-production"
    cors_origins: str = "http://localhost:3000"
    database_url: str = "postgresql+psycopg://vfive:vfive@localhost:5432/vfive"
    legacy_data_file: str = "data/cms_store.json"

    cloudinary_cloud_name: str = ""
    cloudinary_api_key: str = ""
    cloudinary_api_secret: str = ""
    cloudinary_folder: str = "vfive"
    max_upload_mb: int = 8

    @property
    def cors_origin_list(self) -> list[str]:
        return [o.strip() for o in self.cors_origins.split(",") if o.strip()]

    @property
    def cloudinary_configured(self) -> bool:
        return bool(
            self.cloudinary_cloud_name
            and self.cloudinary_api_key
            and self.cloudinary_api_secret
        )


settings = Settings()
