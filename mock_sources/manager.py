"""Модуль утилит для подключения к БД Postgres."""
from abc import ABC, abstractmethod
import asyncio
from contextlib import asynccontextmanager
from typing import AsyncIterator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
    create_async_engine,
    close_all_sessions
)

from settings import settings


class DBManager(ABC):
    """Базовый класс для менеджеров БД."""

    _db_engine: AsyncEngine | None = None
    _session_factory: async_sessionmaker | None = None
    _scoped_session_factory: async_scoped_session | None = None

    def __new__(cls) -> None:
        """Создать новый экземпляр класса."""
        cls._start_if_does_not_exist()

    @classmethod
    @abstractmethod
    def _create_db_engine(cls) -> AsyncEngine:
        """Создать движок БД."""
        raise NotImplementedError(
            'Нужно явно определить метод создания движка БД'
        )

    @classmethod
    def _start_if_does_not_exist(cls) -> None:
        """Создать движок БД, если он еще не создан."""
        if cls._db_engine is None:
            cls._start_db_engine()

    @classmethod
    def _start_db_engine(cls) -> AsyncEngine:
        """Создать движок БД и сохранить его в атрибут класса."""
        cls._db_engine = cls._create_db_engine()
        cls._session_factory = async_sessionmaker(
            autocommit=False, autoflush=False, bind=cls._db_engine
        )
        cls._scoped_session_factory = async_scoped_session(cls._session_factory, asyncio.current_task)
        return cls._db_engine

    @classmethod
    def get_db_engine(cls) -> AsyncEngine:
        """Получить движок БД."""
        cls._start_if_does_not_exist()
        return cls._db_engine

    @classmethod
    def get_scoped_session_factory(cls) -> async_scoped_session:
        """Получить фабрику скоупед сессий."""
        cls._start_if_does_not_exist()
        return cls._scoped_session_factory

    @classmethod
    def stop_db_engine(cls) -> None:
        """Остановить движок БД."""
        if cls._db_engine is not None:
            close_all_sessions()
            cls._db_engine.dispose()
            cls._db_engine = None


class DBManagerSettings(DBManager):
    """Менеджер для БД, который использует строку подключения из настроек."""

    @classmethod
    def _create_db_engine(cls) -> AsyncEngine:
        """Создать движок БД, используя строку подключения из настроек."""
        return create_async_engine(
            settings.DB_CONNECTION_STRING_TOKEN, echo=settings.DB_ECHO
        )


@asynccontextmanager
async def open_session() -> AsyncIterator[AsyncSession]:
    """Контекстный менеджер сессий."""
    factory = DBManagerSettings.get_scoped_session_factory()
    session = factory()
    yield session
    await session.close()


async def get_session() -> AsyncSession:
    """Получить сессию."""
    async with open_session() as session:
        yield session
