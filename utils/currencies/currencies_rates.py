import time
from typing import List

from utils.helpers.helpers import Helpers
from utils.services_http.exchange_rates_service_http import ExchangeRatesServiceHttp


class CurrenciesRates:

    def __init__(self, exchange_rates_service: ExchangeRatesServiceHttp):
        self.exchange_rates_service = exchange_rates_service

    async def fetch_currencies_rates_for_month(
        self,
        year: int,
        month: int,
    ) -> List[dict]:
        rates_list: List[dict] = []

        days: int = Helpers.get_month_days(year, month)

        for i in range(1, days + 1):
            time.sleep(0.25)
            month: str = f"{month:02}"
            days: str = f"{i:02}"
            endpoint_nbp: str = (
                f"/exchangerates/tables/a/{year}-{month}-{days}/?format=json"
            )
            exchange_rates = await self.exchange_rates_service.fetch_data(
                endpoint=endpoint_nbp
            )
            if exchange_rates:
                rates = exchange_rates[0].rates
                for rate in rates:
                    rate_dict = dict(rate)
                    rates_dict = {
                        "effectiveDate": exchange_rates[0].effective_date,
                        **rate_dict,
                    }
                    rates_list.append(rates_dict)

        return rates_list
