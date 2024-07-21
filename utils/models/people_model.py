from pydantic import BaseModel
from typing import List


class PeopleModel(BaseModel):

    name: str
    height: str
    mass: str
    hair_color: str
    skin_color: str
    eye_color: str
    gender: str
    url: str
    vehicles: List[str]
    films: List[str]

    @classmethod
    def json_deserialize(cls, data):
        return cls(**data)
