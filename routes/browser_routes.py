from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Optional
import json

from db.connector import MongoManager
from dal.queries import EventsDal
from services.external_api_service import ExternalDataLoader, get_loader

browser_router = APIRouter()

MONGO = MongoManager()

@browser_router.get("/events/load_db")
def load_events_to_db(client = Depends(MONGO.get_client)):
    return EventsDal.add_events(client)

@browser_router.get("/events/read_db")
def get_events_from_db(client = Depends(MONGO.get_client)):
    return EventsDal.get_events(client)


@browser_router.get("/events/load_external_data")
def load_events_to_json(url: str | None  = None, params: str | None = Query(None),
                       loader: ExternalDataLoader = Depends(get_loader)
):
    try:
        params = json.loads(params) if params else None
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Params must be valid JSON")

    try:
        file_path = loader.load(url, params)
        return {"success": True, "file_path": file_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to load external data: {str(e)}")
