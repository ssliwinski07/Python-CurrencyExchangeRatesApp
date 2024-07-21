from pydantic import BaseModel, Field

from utils.consts.consts import DATABASE_NAME


class DatabaseConfigModel(BaseModel):

    user: str
    password: str
    host: str
    port: str
    database_name: str = Field(alias=DATABASE_NAME)

    @classmethod
    def json_deserialize(cls, data):
        return cls(**data)
