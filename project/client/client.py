import aiohttp
import logging
from typing import Optional
from settings import settings
from schemas import OrderData, ZoneData, Executor, ConfigMap, TollRoadsData

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class HttpClient:
    session: aiohttp.ClientSession = None

    def start(self):
        self.session = aiohttp.ClientSession()

    async def stop(self):
        await self.session.close()
        self.session = None

    def __call__(self) -> aiohttp.ClientSession:
        assert self.session is not None
        return self.session

    async def get_order_data(self, order_id: str) -> Optional[OrderData]:
        try:
            async with self.session.get(settings.ORDER_URL, params={'id': order_id}) as response:
                response.raise_for_status()
                logger.debug(f"Ответ от сервера получен для заказа {order_id} с кодом: {response.status}")
                data = await response.json()
                zone_id = data.get('zone_id')
                user_id = data.get('user_id')
                base_coin_amount = data.get('base_coin_amount')

                if zone_id is None or user_id is None or base_coin_amount is None:
                    logger.error(f"Ошибка: отсутствуют необходимые поля в ответе для order_id={order_id}")
                    return None

                order_data = OrderData(id=order_id, zone_id=zone_id, user_id=user_id, base_coin_amount=base_coin_amount)
                logger.info(f"Данные для заказа {order_id} успешно получены: {order_data}")
                return order_data

        except aiohttp.ClientError as e:
            logger.error(f"Ошибка при запросе к {settings.ORDER_URL}: {e}")
        except aiohttp.ContentTypeError:
            logger.error(f"Ошибка: ответ от сервера не в формате JSON для order_id={order_id}")
        except Exception as e:
            logger.error(f"Неизвестная ошибка при получении данных для order_id={order_id}: {e}")
        return None

    async def get_zone_info(self, zone_id: str) -> Optional[ZoneData]:
        try:
            async with self.session.get(settings.ZONE_URL, params={'id': zone_id}) as response:
                response.raise_for_status()
                logger.debug(f"Ответ от сервера получен для зоны {zone_id} с кодом: {response.status}")
                data = await response.json()
                coin_coeff = data.get('coin_coeff')
                display_name = data.get('display_name')
                if coin_coeff is None or display_name is None:
                    logger.error(f"Ошибка: отсутствуют необходимые поля в ответе для zone_id={zone_id}")
                    return None

                zone_data = ZoneData(id=zone_id, coin_coeff=coin_coeff, display_name=display_name)
                logger.info(f"Данные для зоны {zone_id} успешно получены: {zone_data}")
                return zone_data

        except aiohttp.ClientError as e:
            logger.error(f"Ошибка при запросе к {settings.ZONE_URL}: {e}")
        except aiohttp.ContentTypeError:
            logger.error(f"Ошибка: ответ от сервера не в формате JSON для zone_id={zone_id}")
        except Exception as e:
            logger.error(f"Неизвестная ошибка при получении данных для zone_id={zone_id}: {e}")
        return None

    async def get_toll_roads(self, zone_display_name: str) -> Optional[TollRoadsData]:
        try:
            async with self.session.get(settings.TOLL_ROADS_URL, params={'zone_display_name': zone_display_name}) as response:
                response.raise_for_status()
                logger.debug(f"Ответ от сервера получен для зоны {zone_display_name} с кодом: {response.status}")
                data = await response.json()
                bonus_amount = data.get('bonus_amount')

                if bonus_amount is None:
                    logger.error(f"Ошибка: отсутствует поле 'bonus_amount' в ответе для зоны {zone_display_name}")
                    return None

                toll_roads_data = TollRoadsData(bonus_amount=bonus_amount)
                logger.info(f"Данные для зоны {zone_display_name} успешно получены: {toll_roads_data}")
                return toll_roads_data

        except aiohttp.ClientError as e:
            logger.error(f"Ошибка при запросе к {settings.TOLL_ROADS_URL}: {e}")
        except aiohttp.ContentTypeError:
            logger.error(f"Ошибка: ответ от сервера не в формате JSON для зоны {zone_display_name}")
        except Exception as e:
            logger.error(f"Неизвестная ошибка при получении данных для зоны {zone_display_name}: {e}")
        return None

    async def get_executor_profile(self, executor_id: str) -> Optional[Executor]:
        try:
            async with self.session.get(settings.EXECUTOR_URL, params={'id': executor_id}) as response:
                response.raise_for_status()
                logger.debug(f"Ответ от сервера получен для исполнителя {executor_id} с кодом: {response.status}")
                data = await response.json()
                tags = data.get('tags')
                rating = data.get('rating')
                if tags is None or rating is None:
                    logger.error(f"Ошибка: отсутствуют необходимые поля в ответе для executor_id={executor_id}")
                    return None

                executer_profile = Executor(id=executor_id, tags=tags, rating=rating)
                logger.info(f"Данные для исполнителя {executor_id} успешно получены: {executer_profile}")
                return executer_profile

        except aiohttp.ClientError as e:
            logger.error(f"Ошибка при запросе к {settings.EXECUTOR_URL}: {e}")
        except aiohttp.ContentTypeError:
            logger.error(f"Ошибка: ответ от сервера не в формате JSON для executor_id={executor_id}")
        except Exception as e:
            logger.error(f"Неизвестная ошибка при получении данных для executor_id={executor_id}: {e}")
        return None

    async def get_configs(self) -> Optional[ConfigMap]:
        try:
            async with self.session.get(settings.CONFIG_URL) as response:
                response.raise_for_status()
                logger.debug(f"Ответ от сервера получен с кодом: {response.status}")
                data = await response.json()
                config_map = ConfigMap(data=data)
                logger.info("Конфигурации успешно получены.")
                return config_map

        except aiohttp.ClientError as e:
            logger.error(f"Ошибка при запросе к {settings.CONFIG_URL}: {e}")
        except aiohttp.ContentTypeError:
            logger.error(f"Ошибка: ответ от сервера не в формате JSON.")
        except Exception as e:
            logger.error(f"Неизвестная ошибка при получении конфигураций: {e}")
        return None
