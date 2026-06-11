from fastapi import APIRouter

from app.schemas.common import ApiResponse
from app.schemas.recommendation import RecommendationRequest, RecommendationResult
from app.services.recommendation_service import recommend_laptops as recommend_service
from app.utils.response import success_response

router = APIRouter(tags=["Recommendations"])


@router.post("/recommendations", response_model=ApiResponse[RecommendationResult])
async def recommend_laptops(payload: RecommendationRequest) -> dict[str, object]:
    """Create laptop recommendations from validated user preferences."""
    result = recommend_service(payload).model_dump()
    return success_response(result["message"], result)
