from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://postgres:pass@localhost:5432/genai"
    SECRET_KEY: str = "CHANGE_ME"
    OPENAI_API_KEY: str | None = None
    REDIS_URL: str = "redis://localhost:6379/0"
    RAG_DOCS_PATH: str = "./data/docs"

    class Config:
        env_file = ".env"

settings = Settings()
