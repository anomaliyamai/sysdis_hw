from generic_repository import TableRepository
from models import AssignedOrder


class AssignedOrderRepository(TableRepository):
    type_ = AssignedOrder
