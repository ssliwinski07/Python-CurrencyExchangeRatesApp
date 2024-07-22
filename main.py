import asyncio
import json
from typing import List

from utils.currencies.currencies_rates import CurrenciesRates
from utils.helpers.helpers import Helpers
from utils.services_http.exchange_rates_service_http import ExchangeRatesServiceHttp
from utils.database.database_operations import DatabaseOperations


async def get_data():

    exchange_rates_service: ExchangeRatesServiceHttp = ExchangeRatesServiceHttp()

    while True:
        try:
            month_input = input("Enter month (1-12): ")
            year_input = input("Enter year: ")
            rates_input = input("Rates to check. Separate them with ','.): ")

            if not month_input.isdigit() or not year_input.isdigit():
                print("Wrong value, please provide a valid number.")
                continue

            month_input_int = int(month_input)
            year_input_int = int(year_input)
            rates_input_list = rates_input.split(",")
            rates_input_list = [rate.strip().upper() for rate in rates_input_list]

            if month_input_int < 1 or month_input_int > 12:
                print("Invalid month. Please enter a number between 1 and 12.")
                continue

            currencies_rates: List[dict] = await CurrenciesRates(
                exchange_rates_service=exchange_rates_service
            ).fetch_currencies_rates_for_month(
                year=year_input_int,
                month=month_input_int,
                rates_to_look=rates_input_list,
            )

            # print(json.dumps(currencies_rates, indent=4))
            insert_data(data=currencies_rates)

            is_continue = (
                input('Do you want to continue (if so, write "yes")? ').strip().lower()
            )

            if is_continue != "yes":
                break

            Helpers.clear_screen()
        except Exception as e:
            print(f"Error: {e}")


def insert_data(data):
    db_ops: DatabaseOperations = DatabaseOperations(
        config_path="configs/db_config.json"
    )
    query: str = (
        'INSERT INTO exchangerates ("effectivedate", "currency", "code", "mid") VALUES (:effectiveDate, :currency, :code, :mid)'
    )

    connection = db_ops.open_db_connection()
    if connection:
        db_ops.insert_data(query=query, connection=connection, data=data)
        db_ops.close_db_connection(db_connection=connection)
    else:
        print("No connection with db")


async def main():
    await get_data()


if __name__ == "__main__":
    asyncio.run(main())
