from fastapi import APIRouter, Depends, HTTPException
from http import HTTPStatus
from sqlalchemy.ext.asyncio import AsyncSession
from crud import AssignedOrderRepository
from manager import get_session
from models import AssignedOrder as AssignedOrderModel

get_order_router = APIRouter(
    prefix='/get-order',
    tags=['Order']
)


@get_order_router.get('/{order_id}')
async def get_order_data(order_id: int, session: AsyncSession = Depends(get_session)):
    db = AssignedOrderRepository(session)
    result = await db.get_by_id(AssignedOrderModel(order_id=order_id))
    if not result:
        return HTTPException(status_code=HTTPStatus.BAD_REQUEST)
    return result
