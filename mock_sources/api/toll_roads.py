from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from crud import TollRoadsRepository
from manager import get_session
from models import TollRoad as TollRoadModel
from schemas import TollRoadsCreate, TollRoads


tollroads_router = APIRouter(
    prefix='/toll-roads',
    tags=['TollRoads']
)


@tollroads_router.post('')
async def create_toll_roads_data(toll_roads: TollRoadsCreate, session: AsyncSession = Depends(get_session)):
    db = TollRoadsRepository(session)
    await db.create(TollRoadModel(**toll_roads.model_dump()))


@tollroads_router.get('', response_model=TollRoads)
async def get_toll_roads_data(id_: int, session: AsyncSession = Depends(get_session)):
    db = TollRoadsRepository(session)
    return await db.get_by_id(id_)


@tollroads_router.delete('')
async def delete_toll_roads_data(id_: int, session: AsyncSession = Depends(get_session)):
    db = TollRoadsRepository(session)
    await db.delete(await db.get_by_id(id_))
