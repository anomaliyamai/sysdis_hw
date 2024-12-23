import asyncio
import aiohttp
import logging
from pydantic_settings import BaseSettings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    DB_CONNECTION_STRING_TOKEN: str = "postgresql+asyncpg://pguser:pgpass@psql-db-service:5432/db"
    DB_ECHO: bool = False
    PORT: int = 9000
    HOST: str = "0.0.0.0"
    ORDER_URL: str = 'http://localhost:3629/order-data'
    ZONE_URL: str = 'http://localhost:3629/zone-data'
    EXECUTOR_URL: str = 'http://localhost:3629/executer-profile'
    CONFIG_URL: str = 'http://localhost:3629/configs'
    TOLL_ROADS_URL: str = 'http://localhost:3629/toll-roads'

    async def fetch_config(self):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.CONFIG_URL) as response:
                    response.raise_for_status()
                    data = await response.json()

                    self.ORDER_URL = data.get('order_url', self.ORDER_URL)
                    self.ZONE_URL = data.get('zone_url', self.ZONE_URL)
                    self.EXECUTOR_URL = data.get('executor_url', self.EXECUTOR_URL)
                    self.TOLL_ROADS_URL = data.get('toll_roads_url', self.TOLL_ROADS_URL)
                    self.DB_CONNECTION_STRING_TOKEN = data.get('db_connection_string_token',
                                                               self.DB_CONNECTION_STRING_TOKEN)

                    logger.info("Settings updated.")
        except Exception as e:
            logger.error(f"Error fetching config: {e}")

    async def update_config_periodically(self):
        while True:
            await self.fetch_config()
            await asyncio.sleep(60)

    async def start_update_loop(self):
        await self.fetch_config()
        await self.update_config_periodically()


settings = Settings()
