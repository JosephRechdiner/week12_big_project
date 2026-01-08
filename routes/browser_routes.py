from fastapi import APIRouter, Depends
from db.connector import MongoManager
from utils import read_json
import os

browser_router = APIRouter()

MONGO = MongoManager()
MONGO_INITDB_DATABASE = os.getenv("MONGO_INITDB_DATABASE")
COLLECTION = "events"

@browser_router.get("/events")
def load_events_to_db(client = Depends(MONGO.get_client())):
    data = read_json()
    db = client[MONGO_INITDB_DATABASE]
    collection = db[COLLECTION]
    collection.insert_many(data)
    return {"msg": "ok"}

@browser_router.get("/events")
def get_events(client = Depends(MONGO.get_client())):
    all_events = []
    db = client[MONGO_INITDB_DATABASE]
    collection = db[COLLECTION]
    for event in collection.find({}):
        all_events.append(event)
    return all_events