from pydantic import BaseModel


class BaseTollRoads(BaseModel):
    bonus_amount: float


class TollRoadsCreate(BaseTollRoads):
    ...


class TollRoads(BaseTollRoads):
    id: str
