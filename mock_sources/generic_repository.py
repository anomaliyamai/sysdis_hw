from sqlalchemy.ext.asyncio import AsyncSession

from typing import Generic, TypeVar

T = TypeVar("T")


class TableRepository(Generic[T]):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, entity: T) -> None:
        self.session.add(entity)
        await self.session.commit()

    async def update(self, entity: T) -> None:
        await self.session.merge(entity)
        await self.session.commit()

    async def delete(self, entity: T) -> None:
        await self.session.delete(entity)
