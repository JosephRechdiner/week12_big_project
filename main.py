from fastapi import FastAPI
import os

from routes.browser_routes import browser_router
from db.connector import MongoManager
from constants import DATA_PATH


from routes.browser_routes import browser_router
from db.connector import MongoManager
app = FastAPI()

@app.on_event("startup")
def startup_event():
    MongoManager()
    os.makedirs(DATA_PATH, exist_ok=True)

@app.on_event("shutdown")
def shutdown_db_client():
    MongoManager().close()

app.include_router(browser_router)