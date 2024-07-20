import sqlalchemy as sql
from sqlalchemy.exc import SQLAlchemyError
import yaml
import asyncio

from lib.consts.consts import ENCODING_UTF

### TO DO
## 1. In method __create_connection_string do the get the data from json file, instead of yaml + create class
# ConfigModel with with properties db_name, db_user etc. + using json serialization fill the object with data from json file
## 2. Add method to insert data to db
## 3. Think about adding connection close to the method to insert data to db


class DatabaseOperations:

    def __init__(self, config_path: str):
        self.config_path: str = config_path

    def open_db_connection(self) -> sql.Connection:

        try:
            connection_string: str = self.__create_connection_string()
            db_engine = sql.create_engine(connection_string)
            connection = db_engine.connect()
            return connection
        except SQLAlchemyError as error:
            print(f"Error occured: {error}")

    def close_db_connection(self, db_connection: sql.Connection):
        db_connection.close()

    def __create_connection_string(self) -> str:
        config_file: dict = self.__get_config_file()
        connection_string: str = (
            f"postgresql+psycopg2://{config_file['db_user']}:{config_file['db_pass']}@{config_file['db_host']}:{config_file['db_port']}/{config_file['db_name']}"
        )

        return connection_string

    def __get_config_file(self) -> dict:
        config_file: dict = {}

        with open(self.config_path, "r", encoding=ENCODING_UTF) as f:
            config_file = yaml.safe_load(f)

        return config_file
