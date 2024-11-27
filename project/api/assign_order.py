from datetime import datetime
from pydantic import BaseModel
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from crud import AssignedOrderRepository
from manager import get_session
from models import AssignedOrder as AssignedOrderModel


class Identificators(BaseModel):
    order_id: int
    executor_id: int


assign_order_router = APIRouter(
    prefix='/assign-order',
    tags=['Order']
)


@acquire_order_router.post('')
async def assign_data(identificators: Identificators, session: AsyncSession = Depends(get_session)):
    db = AssignedOrderRepository(session)
    result = await db.create(
        AssignedOrderModel(order_id=identificators.order_id, executor_id=identificators.executor_id,
                           assign_time=datetime.now()))
    return result
