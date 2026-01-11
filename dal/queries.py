from utils import read_json
import os

MONGO_INITDB_DATABASE = os.getenv("MONGO_INITDB_DATABASE")
COLLECTION = "events"

class EventsDal:
    @staticmethod
    def add_events(client):
        data = read_json()
        if data:
            db = client[MONGO_INITDB_DATABASE]
            collection = db[COLLECTION]
            collection.insert_many(data)
            return {"msg": "Data inserted!"}
        return {"msg": "No data available"}

    @staticmethod
    def get_events(client):
        all_events = []
        db = client[MONGO_INITDB_DATABASE]
        collection = db[COLLECTION]
        for event in collection.find({}):
            event["_id"] = str(event["_id"])
            all_events.append(event)
        return all_events