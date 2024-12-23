import asyncio
from collections.abc import Coroutine
from socket import AF_INET
from typing import List, Optional, Any, Dict

import aiohttp
from fastapi import FastAPI
from fastapi.logger import logger as fastAPI_logger
from fastapi.requests import Request
from fastapi.responses import Response

SIZE_POOL_AIOHTTP = 100


class SingletonAiohttp:
    aiohttp_client: Optional[aiohttp.ClientSession] = None

    @classmethod
    def get_aiohttp_client(cls) -> aiohttp.ClientSession:
        if cls.aiohttp_client is None:
            timeout = aiohttp.ClientTimeout(total=2)
            connector = aiohttp.TCPConnector(family=AF_INET, limit_per_host=SIZE_POOL_AIOHTTP)
            cls.aiohttp_client = aiohttp.ClientSession(timeout=timeout, connector=connector)

        return cls.aiohttp_client

    @classmethod
    async def close_aiohttp_client(cls) -> None:
        if cls.aiohttp_client:
            await cls.aiohttp_client.close()
            cls.aiohttp_client = None

    @classmethod
    async def query_url(cls, url: str) -> Any:
        client = cls.get_aiohttp_client()

        try:
            async with client.post(url) as response:
                if response.status != 200:
                    return {"ERROR OCCURED" + str(await response.text())}

                json_result = await response.json()
        except Exception as e:
            return {"ERROR": e}

        return json_result


async def on_start_up() -> None:
    fastAPI_logger.info("on_start_up")
    SingletonAiohttp.get_aiohttp_client()


async def on_shutdown() -> None:
    fastAPI_logger.info("on_shutdown")
    await SingletonAiohttp.close_aiohttp_client()


app = FastAPI(docs_url="/docs", on_startup=[on_start_up], on_shutdown=[on_shutdown])


@app.get('/endpoint')
async def endpoint() -> Any:
    url = "http://example.com"
    return await SingletonAiohttp.query_url(url)


@app.get('/endpoint_multi')
async def endpoint_multi() -> Dict[str, int]:
    url = "http://localhost:8080/test"

    async_calls: List[Coroutine[Any, Any, Any]] = list()

    async_calls.append(SingletonAiohttp.query_url(url))
    async_calls.append(SingletonAiohttp.query_url(url))

    all_results: List[Dict[Any, Any]] = await asyncio.gather(*async_calls)
    return {'success': sum([x['success'] for x in all_results])}


@app.post("/endpoint_stream/")
async def endpoint_stream(request: Request):
    body = b'RST'
    async for chunk in request.stream():
        body += chunk

    return Response(body, media_type='text/plain')


if __name__ == '__main__':  # local dev
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)