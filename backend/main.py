from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.endpoints import auth
from app.core.config import settings

app = FastAPI(
    title="Finance App API",
    description="Backend for personal finance management application",
    version="0.1.0"
)

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В продакшене заменить на конкретные домены
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем роутеры
app.include_router(auth.router, prefix="/api/v1/auth", tags=["authentication"])

@app.get("/")
def root():
    return {"message": "Finance API is running"}

@app.get("/health")
def health_check():
    return {"status": "ok"}