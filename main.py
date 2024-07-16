import asyncio
from typing import List


from utils.models.exchange_rates_model import ExchangeRatesModel
from utils.services_http.exchange_rates_service_http import ExchangeRatesServiceHttp
from utils.models.people_model import PeopleModel
from utils.services_http.people_service_http import PeopleServiceHttp


async def main():

    exchange_rates_service: ExchangeRatesServiceHttp = ExchangeRatesServiceHttp()
    people_service: PeopleServiceHttp = PeopleServiceHttp()

    endpoint_nbp: str = "/exchangerates/tables/a/2029-06-05/?format=json"
    endpoint_swapi: str = "/people/1/"

    people: PeopleModel = await people_service.fetch_data(endpoint=endpoint_swapi)

    print(people.name)


if __name__ == "__main__":
    asyncio.run(main())
