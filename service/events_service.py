from utils import read_json
from dal.queries import EventsDal

class EventsService:
    @staticmethod
    def get_events_service(client):
        return EventsDal.get_events(client)
    
    @staticmethod
    def add_events_service(client):
        data = read_json()
        has_inserted = EventsDal.add_events(client, data)
        if has_inserted:
            return {"msg": "Data inserted"}
        return {"msg": "No data available"}

