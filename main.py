from fastapi import FastAPI


from routes.browser_routes import browser_router
from db.connector import MongoManager
app = FastAPI()

@app.on_event("startup")
def startup_event():
    MongoManager()

app.include_router(browser_router)