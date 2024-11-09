from generic_repository import TableRepository
from models import Zone


class ZoneRepository(TableRepository):
    type_ = Zone
