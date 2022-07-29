from pymongo import MongoClient
from src.configs.database_configs import database_infos


class __DBConnectionHandler:

    def __init__(self):
        self.client = None
        self.database = None
        username = database_infos["USERNAME"]
        if username:
            username_password = f"{username}:{database_infos['PASSWORD']}@"
        else:
            username_password = ""
        port = database_infos["PORT"]
        if port:
            port = f":{port}"
        else:
            port = ""
        self.__connection_string = f"mongodb://{username_password}{database_infos['HOST']}{port}"

    def connect_to_bd(self):
        self.client = MongoClient(self.__connection_string)
        self.database = self.client.get_database(database_infos["DB_NAME"])

    def get_collection(self, collection):
        return self.database.get_collection(collection)


db_connection_handler = __DBConnectionHandler()
