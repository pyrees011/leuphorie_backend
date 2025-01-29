from fastapi import FastAPI
from routes import router  # Import the combined router

app = FastAPI(title="Settings Service API")

app.include_router(router)
