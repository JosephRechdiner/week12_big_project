from fastapi import APIRouter, Depends
from db.connector import MongoManager
from dal.queries import EventsDal

browser_router = APIRouter()

MONGO = MongoManager()

@browser_router.get("/events/load_db")
def load_events_to_db(client = Depends(MONGO.get_client)):
    return EventsDal.add_events(client)

@browser_router.get("/events/read_db")
def get_events_from_db(client = Depends(MONGO.get_client)):
    return EventsDal.get_events(client)