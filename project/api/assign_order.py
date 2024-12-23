import uuid
from datetime import datetime
from http import HTTPStatus
from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from crud import AssignedOrderRepository
from manager import get_session
from models import AssignedOrder as AssignedOrderModel


class Identificators(BaseModel):
    order_id: str
    executor_id: int


assign_order_router = APIRouter(
    prefix='/assign-order',
    tags=['Order']
)


@assign_order_router.post('')
async def assign_data(identificators: Identificators, session: AsyncSession = Depends(get_session)):
    db = AssignedOrderRepository(session)
    res = await db.get_by_id(identificators.order_id)
    if not res:
        return await db.create(
            AssignedOrderModel(order_id=identificators.order_id, executor_id=identificators.executor_id,
                               assign_time=datetime.utcnow()))
    raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="order already created")
