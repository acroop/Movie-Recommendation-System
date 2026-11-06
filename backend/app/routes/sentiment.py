from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.sentiment_service import (
    SentimentService
)


router = APIRouter(
    prefix="/sentiment",
    tags=["Sentiment"]
)


sentiment_service = SentimentService()


class SentimentRequest(BaseModel):

    review: str


@router.post("")
def analyze_sentiment(
    request: SentimentRequest
):

    try:

        result = sentiment_service.predict(
            request.review
        )

        return result

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )