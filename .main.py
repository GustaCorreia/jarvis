from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description="Projeto Jarvis"
)


@app.get("/")
async def root():
    return {
        "project": settings.APP_NAME,
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT,
        "status": "online"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }
