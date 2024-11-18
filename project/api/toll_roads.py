from fastapi import APIRouter, Depends, HTTPException
from http import HTTPStatus
from sqlalchemy.ext.asyncio import AsyncSession
from client import HttpClient
from crud import AssignedOrderRepository
from manager import get_session
from models import AssignedOrder as AssignedOrderModel

http_client = HttpClient()

tollroads_router = APIRouter(
    prefix='/toll-roads',
    tags=['TollRoads']
)


@tollroads_router.get('/{zone_display_name}')
async def get_and_update_toll_roads_data(zone_display_name: str,
                                         session: AsyncSession = Depends(get_session)):
    toll_roads_data = await http_client.get_toll_roads(zone_display_name)
    if not toll_roads_data:
        return HTTPException(status_code=HTTPStatus.BAD_REQUEST)
    db = AssignedOrderRepository(session)
    return await db.update(AssignedOrderModel(coin_bonus_amount=toll_roads_data.bonus_amount))
