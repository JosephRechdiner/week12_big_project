from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os

MONGO_INITDB_ROOT_USERNAME = os.getenv("MONGO_INITDB_ROOT_USERNAME")
MONGO_INITDB_ROOT_PASSWORD = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
MONGO_HOST =  os.getenv("MONGO_HOST")
MONGO_PORT = os.getenv("MONGO_PORT")

class MongoManager:
    def __init__(self):
        self.config = {
            "host": MONGO_HOST,
            "port": MONGO_PORT,
            "username": MONGO_INITDB_ROOT_USERNAME,
            "password": MONGO_INITDB_ROOT_PASSWORD,
        }

    def get_client(self):
        try:
            client = MongoClient(**self.config)
            return client
        except ConnectionFailure as e:
            print(f"Connection failed! {e}")

         