import asyncio
from typing import List


from utils.models.exchange_rates_model import ExchangeRatesModel
from utils.services_http.exchange_rates_service_http import ExchangeRatesServiceHttp


async def main():

    exchange_rates_service: ExchangeRatesServiceHttp = ExchangeRatesServiceHttp()

    exchange_rates: List[ExchangeRatesModel] = exchange_rates_service.fetch_data()

    print(exchange_rates[0].effective_date)


if __name__ == "__main__":
    asyncio.run(main())
