from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from http import HTTPStatus
from sqlalchemy.ext.asyncio import AsyncSession
from crud import AssignedOrderRepository
from manager import get_session
from models import AssignedOrder as AssignedOrderModel

acquire_order_router = APIRouter(
    prefix='/acquire-order',
    tags=['Order']
)


@acquire_order_router.post('/{executor_id}')
async def acquire_data(executor_id: int, session: AsyncSession = Depends(get_session)):
    db = AssignedOrderRepository(session)
    res = await db.get_by_executor_id(executor_id)
    res.acquire_time = datetime.utcnow()
    result = await db.update(res)
    return result
