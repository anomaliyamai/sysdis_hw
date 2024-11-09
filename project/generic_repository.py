from sqlalchemy.ext.asyncio import AsyncSession

from typing import Generic, TypeVar

T = TypeVar("T")


class TableRepository(Generic[T]):
    type_ = None

    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    async def get_by_id(self, id_: int) -> T | None:
        return await self.session.get(self.type_, id_)

    async def create(self, entity: T) -> T:
        self.session.add(entity)
        await self.session.commit()
        return entity

    async def update(self, entity: T) -> None:
        await self.session.merge(entity)
        await self.session.commit()

    async def delete(self, entity: T) -> None:
        await self.session.delete(entity)
        await self.session.commit()
