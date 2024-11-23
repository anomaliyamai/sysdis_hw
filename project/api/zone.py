from fastapi import APIRouter, Depends, HTTPException
from http import HTTPStatus
from sqlalchemy.ext.asyncio import AsyncSession
from client import HttpClient
from crud import AssignedOrderRepository
from manager import get_session
from models import AssignedOrder as AssignedOrderModel

http_client = HttpClient()

zone_router = APIRouter(
    prefix='/zone-data',
    tags=['Zone']
)


@zone_router.get('/{zone_id}')
async def get_and_update_zone_data(zone_id: str, session: AsyncSession = Depends(get_session)):
    zone_data = await http_client.get_zone_info(zone_id)
    if not zone_data:
        return HTTPException(status_code=HTTPStatus.BAD_REQUEST)
    db = AssignedOrderRepository(session)
    return await db.update(AssignedOrderModel(coin_coeff=zone_data.coin_coeff))
