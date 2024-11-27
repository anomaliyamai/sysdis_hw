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
    result = await db.update(AssignedOrderModel(executor_id=executor_id, acquire_time=datetime.now()))
    if not result:
        return HTTPException(status_code=HTTPStatus.BAD_REQUEST)
    return result
