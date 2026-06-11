from fastapi import APIRouter

from app.core.config import get_settings
from app.core.paths import FRONTEND_OPTIONS_PATH, MODEL_METADATA_PATH
from app.schemas.common import ApiResponse
from app.services.data_loader import dataset_exists
from app.services.model_loader import model_exists
from app.utils.response import success_response

router = APIRouter(tags=["Health"])


@router.get("/health", response_model=ApiResponse[dict[str, object]])
async def health_check() -> dict[str, object]:
    """Return application and artifact availability status."""
    settings = get_settings()
    dataset_available = dataset_exists()
    model_available = model_exists()
    options_available = FRONTEND_OPTIONS_PATH.is_file()
    metadata_available = MODEL_METADATA_PATH.is_file()
    is_ready = (
        dataset_available
        and model_available
        and options_available
        and metadata_available
    )

    return success_response(
        "API berjalan.",
        {
            "app_name": settings.app_name,
            "app_version": settings.app_version,
            "dataset_available": dataset_available,
            "model_available": model_available,
            "options_available": options_available,
            "metadata_available": metadata_available,
            "status": "ready" if is_ready else "degraded",
        },
    )
