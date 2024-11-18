from fastapi import APIRouter, Depends, HTTPException
from http import HTTPStatus
from sqlalchemy.ext.asyncio import AsyncSession
from client import HttpClient
from crud import AssignedOrderRepository
from manager import get_session
from models import AssignedOrder as AssignedOrderModel

http_client = HttpClient()

executor_router = APIRouter(
    prefix='/executor-data',
    tags=['Executor']
)


@executor_router.get('/{executor_id}')
async def get_and_update_executor_data(executor_id: str,
                                       session: AsyncSession = Depends(get_session)):
    executor = await http_client.get_executor_profile(executor_id)
    if not executor:
        return HTTPException(status_code=HTTPStatus.BAD_REQUEST)
    db = AssignedOrderRepository(session)
    return await db.update(AssignedOrderModel(executor_id=executor.id))
