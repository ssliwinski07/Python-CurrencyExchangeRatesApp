import time
from typing import List

from lib.utils.utilities import Utilities
from lib.services_http.exchange_rates_service_http import ExchangeRatesServiceHttp


class CurrenciesRates:
    exchange_rates_service: ExchangeRatesServiceHttp = ExchangeRatesServiceHttp()

    @classmethod
    async def fetch_currencies_rates_for_month(
        self,
        year: int,
        month: int,
        rates_to_look: list,
    ) -> List[dict]:
        rates_dict = {}
        rates_list: List[dict] = []

        days: int = Utilities.get_month_days(year, month)

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
                    if rate.code in rates_to_look:
                        rate_dict = dict(rate)
                        rates_dict = {
                            "effectiveDate": exchange_rates[0].effective_date,
                            **rate_dict,
                        }
                        # print(rates_dict)
                        rates_list.append(rates_dict)

        return rates_list
