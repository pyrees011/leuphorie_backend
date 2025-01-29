from fastapi import FastAPI
from app.routes.settings import router as settings_router

app = FastAPI(title="Settings Service API")

app.include_router(settings_router)
