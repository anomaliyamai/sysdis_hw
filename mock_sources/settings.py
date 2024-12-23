from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_CONNECTION_STRING_TOKEN: str = "postgresql+asyncpg://pguser:pgpass@mock-db-service:5432/mock_db"
    DB_ECHO: bool = False


settings = Settings()
