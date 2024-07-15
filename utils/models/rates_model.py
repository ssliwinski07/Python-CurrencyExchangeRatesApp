from dataclasses import dataclass, asdict
import json
from typing import Type, TypeVar
from pydantic import BaseModel


@dataclass
class RatesModel(BaseModel):

    currency: str
    code: str
    mid: float
