from fastapi import APIRouter, Depends, HTTPException
from http import HTTPStatus
from sqlalchemy.ext.asyncio import AsyncSession
from client import HttpClient
from crud import AssignedOrderRepository
from manager import get_session
from models import AssignedOrder as AssignedOrderModel

http_client = HttpClient()

order_router = APIRouter(
    prefix='/order-data',
    tags=['Order']
)


@order_router.get('/{order_id}')
async def get_and_update_order_data(order_id: str,
                                    session: AsyncSession = Depends(get_session)):
    order_data = await http_client.get_order_data(order_id)
    if not order_data:
        return HTTPException(status_code=HTTPStatus.BAD_REQUEST)
    db = AssignedOrderRepository(session)
    return await db.update(AssignedOrderModel(order_id=order_data.id))
