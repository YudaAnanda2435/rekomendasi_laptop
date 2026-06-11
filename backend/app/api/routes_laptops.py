from fastapi import APIRouter, Query

from app.schemas.common import ApiResponse
from app.schemas.laptop import LaptopListData
from app.services.laptop_service import get_laptops
from app.utils.response import success_response

router = APIRouter(tags=["Laptops"])


@router.get("/laptops", response_model=ApiResponse[LaptopListData])
async def list_laptops(
    limit: int = Query(default=20, ge=1, le=100),
    brand: str | None = Query(default=None),
    kebutuhan: str | None = Query(default=None),
    search: str | None = Query(default=None),
) -> dict[str, object]:
    """Return a concise laptop list for frontend browsing."""
    result = get_laptops(
        limit=limit,
        brand=brand,
        kebutuhan=kebutuhan,
        search=search,
    )
    return success_response("Daftar laptop berhasil dimuat.", result)
