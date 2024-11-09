from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_CONNECTION_STRING_TOKEN: str = "postgresql+asyncpg://pguser:pgpass@localhost:5432/db"
    DB_ECHO: bool = False


settings = Settings()
