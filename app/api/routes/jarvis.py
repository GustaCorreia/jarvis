from fastapi import APIRouter

from app.services.jarvis_service import JarvisService

router = APIRouter(
    prefix="/jarvis",
    tags=["Jarvis"],
)

service = JarvisService()


@router.get("/")
def about():
    """
    Retorna informações institucionais do Jarvis.
    """
    return service.about()
