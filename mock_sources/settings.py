from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_CONNECTION_STRING_TOKEN: str = "postgresql+asyncpg://pguser:pgpass@localhost:5433/mock_db"
    DB_ECHO: bool = False


settings = Settings()
