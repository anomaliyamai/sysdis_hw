from pydantic import BaseModel


class BaseZone(BaseModel):
    coin_coeff: float
    display_name: str


class ZoneCreate(BaseZone):
    ...


class Zone(BaseZone):
    id: int
