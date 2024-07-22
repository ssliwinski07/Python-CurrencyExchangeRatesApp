import sqlalchemy as sql
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
import json

from utils.consts.consts import ENCODING_UTF, ENCRYPTION_KEY
from utils.models.database_config_model import DatabaseConfigModel
from utils.encryptions.encryption import Encryption


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

        try:
            db_connection.close()
            print("Connection successfully closed")
        except Exception as e:
            print(f"Error occured: {e}")

    def check_db_connection(self) -> bool:

        try:
            connection = self.open_db_connection()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            self.close_db_connection(db_connection=connection)

    def insert_data(self, query: str, data, connection: sql.Connection):
        try:
            connection.execute(text(query), data)
            connection.commit()
            print("Data inserted succesfully")
        except SQLAlchemyError as e:
            print(f"Error: {e}")

    def __create_connection_string(self) -> str:
        connection_string: str
        config: DatabaseConfigModel = self.__get_config()

        if config != None:
            decrypted_pwd = Encryption.decrypt_password(
                encrypted_password=config.password, key=ENCRYPTION_KEY
            )

            connection_string = f"postgresql+psycopg2://{config.user}:{decrypted_pwd}@{config.host}:{config.port}/{config.database_name}"

        return connection_string

    def __get_config(self) -> DatabaseConfigModel:
        config: DatabaseConfigModel = None

        with open(self.config_path, "r", encoding=ENCODING_UTF) as f:
            loaded_data = json.load(f)
            config = DatabaseConfigModel.json_deserialize(loaded_data)

        return config
