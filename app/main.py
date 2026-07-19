from fastapi import FastAPI

app = FastAPI(
    title="Jarvis",
    version="0.1.0",
    description="Assistente Inteligente"
)


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
