from fastapi import APIRouter, Depends, HTTPException
from http import HTTPStatus
from sqlalchemy.ext.asyncio import AsyncSession
from crud import AssignedOrderRepository
from manager import get_session
from models import AssignedOrder as AssignedOrderModel

cancel_order_router = APIRouter(
    prefix='/delete-order',
    tags=['Order']
)


@acquire_order_router.delete('/{order_id}')
async def delete_data(order_id: int, session: AsyncSession = Depends(get_session)):
    db = AssignedOrderRepository(session)
    delete_status = await db.delete(AssignedOrderModel(order_id=order_id))
    if not delete_status:
        return HTTPException(status_code=HTTPStatus.BAD_REQUEST)
    return delete_status
