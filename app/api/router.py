from fastapi import APIRouter

from app.api.routes.chat import router as chat_router
from app.api.routes.jarvis import router as jarvis_router

api_router = APIRouter()

api_router.include_router(jarvis_router)
api_router.include_router(chat_router)
