import httpx
from typing import List
import requests

from utils.consts.consts import BASE_API
from utils.models.exchange_rates_model import ExchangeRatesModel


class ExchangeRatesServiceHttp:

    api_url = "http://api.nbp.pl/api/exchangerates/tables/a/2024-07-15/?format=json"

    def fetch_data(self):
        response = requests.get(url=self.api_url)
        response.raise_for_status
        data = response.json()
        return data
