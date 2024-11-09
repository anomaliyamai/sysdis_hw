from generic_repository import TableRepository
from models import Order


class OrderRepository(TableRepository):
    type_ = Order
