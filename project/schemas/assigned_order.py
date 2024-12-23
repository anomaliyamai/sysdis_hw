from datetime import datetime

from pydantic import BaseModel


class AssignedOrder(BaseModel):
    order_id: str
    executor_id: int
    coin_coeff: float
    coin_bonus_amount: float
    final_coin_amount: float
    route_information: str
    assign_time: datetime
    acquire_time: datetime


class AssignedOrderCreate(AssignedOrder):
    ...


# class AssignedOrder(BaseAssignedOrder):
#     assign_order_id: str
