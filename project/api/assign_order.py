import uuid
from datetime import datetime
from http import HTTPStatus
from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from crud import AssignedOrderRepository
from manager import get_session
from models import AssignedOrder as AssignedOrderModel
from client import HttpClient
from schemas import ZoneData, OrderData, TollRoadsData


class Identificators(BaseModel):
    order_id: str
    executor_id: int


assign_order_router = APIRouter(
    prefix='/assign-order',
    tags=['Order']
)

http_client = HttpClient()


@assign_order_router.post('')
async def assign_data(identificators: Identificators, session: AsyncSession = Depends(get_session)):
    db = AssignedOrderRepository(session)
    res = await db.get_by_id(identificators.order_id)
    if not res:
        order_data = await http_client.get_order_data("aa")
        if not order_data:
            order_data = OrderData(id="1", user_id="2", zone_id="3", base_coin_amount=1000.2)
        toll_roads_data = await http_client.get_toll_roads("center")
        if not toll_roads_data:
            toll_roads_data = TollRoadsData(bonus_amount=1100.2)
        zone_data = await http_client.get_zone_info("77")
        if not zone_data:
            zone_data = ZoneData(id="3", coin_coeff=5, display_name="msk")
        final_coin_amount = toll_roads_data.bonus_amount + zone_data.coin_coeff * order_data.base_coin_amount
        return await db.create(
            AssignedOrderModel(coin_coeff=zone_data.coin_coeff, order_id=identificators.order_id, executor_id=identificators.executor_id,
                               assign_time=datetime.utcnow(), route_information=zone_data.display_name, final_coin_amount=final_coin_amount,
                               coin_bonus_amount=toll_roads_data.bonus_amount))
    raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="order already created")
