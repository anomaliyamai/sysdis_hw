import asyncio
from fastapi import FastAPI
import uvicorn
from settings import settings
import api

app = FastAPI(title='order_system', docs_url='/docs')


@app.on_event("startup")
async def on_startup():
    asyncio.create_task(settings.start_update_loop())

app.include_router(api.assign_order_router)
app.include_router(api.acquire_order_router)
app.include_router(api.cancel_order_router)
app.include_router(api.executor_router)
app.include_router(api.order_router)
app.include_router(api.tollroads_router)
app.include_router(api.zone_router)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(settings.start_update_loop())
    uvicorn.run('main:app', host=settings.HOST,
                port=settings.PORT)
