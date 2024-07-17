import asyncio
import json
from typing import List

from lib.utils.currencies.currencies_rates import CurrenciesRates


async def main():
    currencies_rates: List[dict] = (
        await CurrenciesRates.fetch_currencies_rates_for_month(
            year=2024, month=6, rates_to_look=["CHF", "USD"]
        )
    )

    print(json.dumps(currencies_rates, indent=4))


if __name__ == "__main__":
    asyncio.run(main())
