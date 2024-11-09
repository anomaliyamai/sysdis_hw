from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from crud import OrderRepository
from manager import get_session
from models import Order as OrderModel
from schemas import OrderCreate, Order


order_router = APIRouter(
    prefix='/order-data',
    tags=['Order']
)


@order_router.post('')
async def create_order_data(order: OrderCreate, session: AsyncSession = Depends(get_session)):
    db = OrderRepository(session)
    await db.create(OrderModel(**order.model_dump()))


@order_router.get('', response_model=Order)
async def get_order_data(id_: int, session: AsyncSession = Depends(get_session)):
    db = OrderRepository(session)
    return await db.get_by_id(id_)


@order_router.delete('')
async def delete_order_data(id_: int, session: AsyncSession = Depends(get_session)):
    db = OrderRepository(session)
    await db.delete(await db.get_by_id(id_))
