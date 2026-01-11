from utils import read_json
import os

MONGO_INITDB_DATABASE = os.getenv("MONGO_INITDB_DATABASE")
COLLECTION = "events"

class EventsDal:
    @staticmethod
    def add_events(client, data):
        if data:
            db = client[MONGO_INITDB_DATABASE]
            collection = db[COLLECTION]
            collection.insert_many(data)
            return True
        return False

    @staticmethod
    def get_events(client):
        all_events = []
        db = client[MONGO_INITDB_DATABASE]
        collection = db[COLLECTION]
        for event in collection.find({}):
            event["_id"] = str(event["_id"])
            all_events.append(event)
        return all_events