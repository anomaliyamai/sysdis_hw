from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from crud import ExecutorRepository
from manager import get_session
from models import Executor as ExecutorModel
from schemas import ExecutorCreate, Executor


executor_router = APIRouter(
    prefix='/executor-data',
    tags=['Executor']
)


@executor_router.post('')
async def create_executor_data(executor: ExecutorCreate, session: AsyncSession = Depends(get_session)):
    db = ExecutorRepository(session)
    await db.create(ExecutorModel(**executor.model_dump()))


@executor_router.get('', response_model=Executor)
async def get_executor_data(id_: int, session: AsyncSession = Depends(get_session)):
    db = ExecutorRepository(session)
    return await db.get_by_id(id_)


@executor_router.delete('')
async def delete_executor_data(id_: int, session: AsyncSession = Depends(get_session)):
    db = ExecutorRepository(session)
    await db.delete(await db.get_by_id(id_))
