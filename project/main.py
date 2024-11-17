from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn

import api


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan, title='project', docs_url='/docs')

app.include_router(api.assigned_order_router)


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000)
