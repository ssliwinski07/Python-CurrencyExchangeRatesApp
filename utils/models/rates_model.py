from dataclasses import dataclass
from pydantic import BaseModel


@dataclass
class RatesModel(BaseModel):

    currency: str
    code: str
    mid: float
