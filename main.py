import asyncio
from typing import List


from utils.models.exchange_rates_model import ExchangeRatesModel
from utils.services_http.exchange_rates_service_http import ExchangeRatesServiceHttp


async def main():

    exchange_rates_service: ExchangeRatesServiceHttp = ExchangeRatesServiceHttp()

    data = exchange_rates_service.fetch_data()


if __name__ == "__main__":
    asyncio.run(main())
