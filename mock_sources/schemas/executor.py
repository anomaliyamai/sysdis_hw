from pydantic import BaseModel


class BaseExecutor(BaseModel):
    tags: list[str]
    rating: float


class ExecutorCreate(BaseExecutor):
    ...


class Executor(BaseExecutor):
    id: str
