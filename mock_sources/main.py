from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn

import api


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan, title='mock_db', docs_url='/docs')

# app.include_router(api.config_map)
app.include_router(api.executor_router)
app.include_router(api.order_router)
app.include_router(api.tollroads_router)
app.include_router(api.zone_router)


if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=8001)
