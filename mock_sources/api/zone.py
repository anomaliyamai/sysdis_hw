from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from crud import ZoneRepository
from manager import get_session
from models import Zone as ZoneModel
from schemas import ZoneCreate, Zone


zone_router = APIRouter(
    prefix='/zone-data',
    tags=['Zone']
)


@zone_router.post('')
async def create_executor_data(zone: ZoneCreate, session: AsyncSession = Depends(get_session)):
    db = ZoneRepository(session)
    await db.create(ZoneModel(**zone.model_dump()))


@zone_router.get('', response_model=Zone)
async def get_executor_data(id_: int, session: AsyncSession = Depends(get_session)):
    db = ZoneRepository(session)
    return await db.get_by_id(id_)


@zone_router.delete('')
async def delete_executor_data(id_: int, session: AsyncSession = Depends(get_session)):
    db = ZoneRepository(session)
    await db.delete(await db.get_by_id(id_))
