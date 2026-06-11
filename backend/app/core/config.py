import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic import BaseModel, field_validator

from app.core.paths import BACKEND_DIR

load_dotenv(BACKEND_DIR / ".env")


class Settings(BaseModel):
    app_name: str = os.getenv("APP_NAME", "Sistem Rekomendasi Laptop API")
    app_version: str = os.getenv("APP_VERSION", "1.0.0")
    api_prefix: str = os.getenv("API_PREFIX", "/api")
    backend_cors_origins: str = os.getenv(
        "BACKEND_CORS_ORIGINS",
        "http://localhost:5173,http://127.0.0.1:5173",
    )

    @field_validator("api_prefix")
    @classmethod
    def validate_api_prefix(cls, value: str) -> str:
        if not value.startswith("/"):
            raise ValueError("API_PREFIX harus diawali dengan '/'.")
        return value.rstrip("/") or "/"

    @property
    def cors_origins(self) -> list[str]:
        return [
            origin.strip()
            for origin in self.backend_cors_origins.split(",")
            if origin.strip()
        ]


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
