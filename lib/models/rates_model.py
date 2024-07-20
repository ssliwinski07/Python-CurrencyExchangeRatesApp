from dataclasses import dataclass, asdict
from pydantic import BaseModel


@dataclass
class RatesModel(BaseModel):

    currency: str
    code: str
    mid: float
