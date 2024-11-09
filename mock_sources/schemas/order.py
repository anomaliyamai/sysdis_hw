from pydantic import BaseModel


class BaseOrder(BaseModel):
    user_id: int
    zone_id: int
    base_coin_amount: float


class OrderCreate(BaseOrder):
    ...


class Order(BaseOrder):
    id: int
