from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from crud import AssignedOrderRepository
from manager import get_session
from models import AssignedOrder as AssignedOrderModel
from schemas import AssignedOrderCreate, AssignedOrder


assigned_order_router = APIRouter(
    prefix='/assigned-order-data',
    tags=['Assigned order']
)


@assigned_order_router.post('')
async def create_order_data(order: AssignedOrderCreate, session: AsyncSession = Depends(get_session)):
    db = AssignedOrderRepository(session)
    await db.create(AssignedOrderModel(**order.model_dump()))


@assigned_order_router.get('', response_model=AssignedOrder)
async def get_order_data(id_: int, session: AsyncSession = Depends(get_session)):
    db = AssignedOrderRepository(session)
    return await db.get_by_id(id_)


@assigned_order_router.delete('')
async def delete_order_data(id_: int, session: AsyncSession = Depends(get_session)):
    db = AssignedOrderRepository(session)
    await db.delete(await db.get_by_id(id_))
