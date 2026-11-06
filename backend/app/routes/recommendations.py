from fastapi import APIRouter, HTTPException

from app.services.recommendation_service import (
    RecommendationService
)


router = APIRouter(
    prefix="/recommend",
    tags=["Recommendations"]
)


recommender = RecommendationService()


@router.get("/{movie_name}")
def recommend(movie_name: str):

    results = recommender.recommend(
        movie_name,
        top_n=10
    )


    if not results:

        raise HTTPException(
            status_code=404,
            detail="Movie not found"
        )


    return {
        "movie": movie_name,
        "recommendations": results
    }