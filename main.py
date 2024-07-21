import asyncio
import json
from typing import List

from utils.currencies.currencies_rates import CurrenciesRates
from utils.helpers.helpers import Helpers
from utils.services_http.exchange_rates_service_http import ExchangeRatesServiceHttp
from utils.models.database_config_model import DatabaseConfigModel
from utils.consts.consts import ENCODING_UTF, ENCRYPTION_KEY
from utils.encryptions.encryption import Encryption


async def main():

    exchange_rates_service: ExchangeRatesServiceHttp = ExchangeRatesServiceHttp()

    while True:
        try:
            month_input = input("Enter month (1-12): ")
            year_input = input("Enter year: ")

            if not month_input.isdigit() or not year_input.isdigit():
                print("Wrong value, please provide a valid number.")
                continue

            month_input_int = int(month_input)
            year_input_int = int(year_input)

            if month_input_int < 1 or month_input_int > 12:
                print("Invalid month. Please enter a number between 1 and 12.")
                continue

            currencies_rates: List[dict] = await CurrenciesRates(
                exchange_rates_service=exchange_rates_service
            ).fetch_currencies_rates_for_month(
                year=year_input_int,
                month=month_input_int,
                rates_to_look=["CHF", "USD"],
            )

            print(json.dumps(currencies_rates, indent=4))

            is_continue = (
                input('Do you want to continue (if so, write "yes")? ').strip().lower()
            )

            if is_continue != "yes":
                break

            Helpers.clear_screen()
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
