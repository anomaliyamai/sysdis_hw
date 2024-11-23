from datetime import datetime
from pydantic import BaseModel


class OrderData(BaseModel):
    id: str
    user_id: str
    zone_id: str
    base_coin_amount: float


class ZoneData(BaseModel):
    id: str
    coin_coeff: float
    display_name: str


class Executor(BaseModel):
    id: str
    tags: list[str]
    rating: float


class TollRoadsData(BaseModel):
    bonus_amount: float


class AssignedOrder(BaseModel):
    assign_order_id: str
    order_id: str
    executer_id: str
    coin_coeff: float
    coin_bonus_amount: float
    final_coin_amount: float
    route_information: str

    assign_time: datetime
    acquire_time: datetime


class ConfigMap:
    def __init__(self, data: dict):
        self._data = data
        for k, v in data.items():
            self.__setattr__(k, v)

    def __getattr__(self, item):
        return self._data.get(item, None)
