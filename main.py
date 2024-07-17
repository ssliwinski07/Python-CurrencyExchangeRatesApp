import asyncio
import json
from typing import List

from lib.utils.currencies.currencies_rates import CurrenciesRates


async def main():

    while True:
        month_input: int = int(input("Enter month: "))
        year_input: int = int(input("Enter year: "))
        currencies_rates: List[dict] = (
            await CurrenciesRates.fetch_currencies_rates_for_month(
                year=year_input, month=month_input, rates_to_look=["CHF", "USD"]
            )
        )
        print(json.dumps(currencies_rates, indent=4))
        break


if __name__ == "__main__":
    asyncio.run(main())
