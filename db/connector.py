from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os
import threading


class MongoManager:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, "client"):
            return  

        self.client = MongoClient(
            host=os.getenv("MONGO_HOST", "localhost"),
            port=int(os.getenv("MONGO_PORT", 27017)),
            username=os.getenv("MONGO_INITDB_ROOT_USERNAME"),
            password=os.getenv("MONGO_INITDB_ROOT_PASSWORD"),        
        )

        # self.db_name = os.getenv("MONGO_INITDB_DATABASE")

        try:
            self.client.admin.command("ping")
            print("MongoDB connected")
        except ConnectionFailure as e:
            raise ConnectionError(f"MongoDB connection failed: {e}")

    def get_client(self) -> MongoClient:
        return self.client

    def get_close(self):
        return self.client.close()

     
