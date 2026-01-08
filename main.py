from fastapi import FastAPI
from routes.browser_routes import browser_router

app = FastAPI()

app.include_router(browser_router)