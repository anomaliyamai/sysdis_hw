from generic_repository import TableRepository
from models import Executor


class ExecutorRepository(TableRepository):
    type_ = Executor
