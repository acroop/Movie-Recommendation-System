from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.recommendations import router as recommendation_router
from app.routes.sentiment import router as sentiment_router


app = FastAPI(
    title="Movie Recommendation API",
    description="Movie recommendation and sentiment analysis API",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    recommendation_router
)

app.include_router(
    sentiment_router
)


@app.get("/")
def root():

    return {
        "message": "Movie Recommendation API is running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }