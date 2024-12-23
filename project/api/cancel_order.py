from datetime import datetime, timedelta, timezone
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


@cancel_order_router.delete('/{order_id}')
async def delete_data(order_id: str, session: AsyncSession = Depends(get_session)):
    db = AssignedOrderRepository(session)
    assigned_order = await db.get_by_id(order_id)
    if assigned_order is None or assigned_order.acquire_time is not None or (
            assigned_order.assign_time - datetime.utcnow().replace(tzinfo=timezone.utc)) > timedelta(minutes=10):
        return HTTPException(status_code=HTTPStatus.BAD_REQUEST)
    delete_status = await db.delete(assigned_order)
    if not delete_status:
        return HTTPException(status_code=HTTPStatus.BAD_REQUEST)
    return delete_status
