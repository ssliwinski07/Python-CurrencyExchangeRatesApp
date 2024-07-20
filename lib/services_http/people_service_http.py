import httpx
from typing import List

from lib.consts.consts import BASE_API_SWAPI
from lib.models.people_model import PeopleModel


class PeopleServiceHttp:

    async def fetch_data(self, endpoint: str) -> PeopleModel:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(f"{BASE_API_SWAPI}{endpoint}")
                response.raise_for_status()
                data = response.json()
                people = PeopleModel.json_deserialize(data=data)
                return people
            except httpx.HTTPStatusError as http_err:
                print(f"HTTP error occurred: {http_err}")
                return None
            except Exception as err:
                print(f"Other error occurred: {err}")
                return None
