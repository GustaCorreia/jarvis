from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import ChatService

router = APIRouter(
    prefix="/api/v1/chat",
    tags=["Chat"],
)

service = ChatService()


@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):
    response = service.chat(request.message)

    return ChatResponse(response=response)
