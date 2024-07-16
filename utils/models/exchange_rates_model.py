import requests
from pydantic import BaseModel, Field
from typing import List

from utils.consts.consts import EFFECTIVE_DATE
from utils.models.rates_model import RatesModel


class ExchangeRatesModel(BaseModel):
    table: str
    no: str
    effective_date: str = Field(alias="effectiveDate")
    rates: List[RatesModel]

    @classmethod
    def json_deserialize(cls, data):
        return cls(**data)
