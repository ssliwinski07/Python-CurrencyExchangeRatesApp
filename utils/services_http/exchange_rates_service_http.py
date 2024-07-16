import httpx
from typing import List

from utils.consts.consts import BASE_API_NBP
from utils.models.exchange_rates_model import ExchangeRatesModel


class ExchangeRatesServiceHttp:

    exchange_rates: List[ExchangeRatesModel] = []

    async def fetch_data(self, endpoint) -> List[ExchangeRatesModel]:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url=f"{BASE_API_NBP}{endpoint}")
                response.raise_for_status
                data = response.json()
                exchange_rates = [ExchangeRatesModel.json_deserialize(data=data[0])]
                return exchange_rates
            except httpx.HTTPStatusError as http_err:
                print(f"HTTP error occurred: {http_err}")
                return self.exchange_rates
            except Exception as err:
                print(f"Other error occurred: {err}")
                return self.exchange_rates
