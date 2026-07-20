from fastapi import FastAPI

from app.api.router import api_router

app = FastAPI(
    title="Jarvis",
    version="0.1.0",
    description="Assistente Inteligente"
)

# Registra todas as rotas da API
app.include_router(api_router)


@app.get("/")
async def root():
    return {
        "message": "Jarvis Online"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }
