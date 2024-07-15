from dataclasses import dataclass, field, asdict
from dataclasses_json import dataclass_json, config
from typing import List
from typing import List, Type, TypeVar
import json
from pydantic import BaseModel

from utils.consts.consts import EFFECTIVE_DATE
from utils.models.rates_model import RatesModel


@dataclass_json
class ExchangeRatesModel(BaseModel):
    table: str
    no: str
    effective_date: str = field(metadata=config(field_name=EFFECTIVE_DATE))
    rates: List[str]
