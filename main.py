import asyncio
from typing import List
import time


from lib.models.exchange_rates_model import ExchangeRatesModel
from lib.services_http.exchange_rates_service_http import ExchangeRatesServiceHttp
from lib.models.people_model import PeopleModel
from lib.services_http.people_service_http import PeopleServiceHttp
from lib.utils.utilities import Utilities


async def main():

    exchange_rates_service: ExchangeRatesServiceHttp = ExchangeRatesServiceHttp()

    notes_dict = {}
    notes_list: List[dict] = []

    year: int = 2024
    month: int = 7

    days: int = Utilities.get_month_days(year, month)

    for i in range(1, days + 1):
        time.sleep(0.25)
        year: str = "2024"
        month: str = f"{month:02}"
        days: str = f"{i:02}"
        endpoint_nbp: str = (
            f"/exchangerates/tables/a/{year}-{month}-{days}/?format=json"
        )
        exchange_rates = await exchange_rates_service.fetch_data(endpoint=endpoint_nbp)
        if exchange_rates:
            rates = exchange_rates[0].rates
            notes_dict["effectiveDate"] = exchange_rates[0].effective_date
            for rate in rates:
                if rate.code == "CHF":
                    notes_dict.update(dict(rate))
            print(notes_dict)


if __name__ == "__main__":
    asyncio.run(main())
