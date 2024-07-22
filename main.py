import asyncio
import json
from typing import List

from utils.currencies.currencies_rates import CurrenciesRates
from utils.helpers.helpers import Helpers
from utils.services_http.exchange_rates_service_http import ExchangeRatesServiceHttp
from utils.database.database_operations import DatabaseOperations


async def get_data(year: int, month: int):

    exchange_rates_service: ExchangeRatesServiceHttp = ExchangeRatesServiceHttp()
    currencies_rates: List[dict] = []

    try:
        print("Fetching data...")
        currencies_rates = await CurrenciesRates(
            exchange_rates_service=exchange_rates_service
        ).fetch_currencies_rates_for_month(
            year=year,
            month=month,
        )
    except Exception as e:
        print(f"Error occured: {e}")

    return currencies_rates


def insert_data(data):
    db_ops: DatabaseOperations = DatabaseOperations(
        config_path="configs/db_config.json"
    )
    query: str = (
        "INSERT INTO exchangerates (effectivedate, currency, code, mid, creationdate) VALUES (:effectiveDate, :currency, :code, :mid, CURRENT_TIMESTAMP)"
    )

    connection = db_ops.open_db_connection()
    if connection:
        db_ops.insert_data(query=query, connection=connection, data=data)
        db_ops.close_db_connection(db_connection=connection)
    else:
        print("No connection with db")


async def main():
    currencies_rates: List[dict]

    while True:
        try:
            month_input = input("Enter month (1-12): ")
            year_input = input("Enter year: ")

            if not month_input.isdigit() or not year_input.isdigit():
                print("Wrong value, please provide a valid number.")
                continue

            currencies_rates = await get_data(
                year=int(year_input), month=int(month_input)
            )

            print(f"Fetched data: \n{json.dumps(currencies_rates, indent=4)}")

            should_insert_data = (
                input(
                    'Do you want to insert fetched data to database? (if so, write "yes", if not write anything else to fetch new data)? '
                )
                .strip()
                .lower()
            )

            if should_insert_data == "yes":
                insert_data(data=currencies_rates)
                break
            else:
                Helpers.clear_screen()
                continue

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
