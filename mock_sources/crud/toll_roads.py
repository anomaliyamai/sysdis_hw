from generic_repository import TableRepository
from models import TollRoad


class TollRoadsRepository(TableRepository):
    type_ = TollRoad
