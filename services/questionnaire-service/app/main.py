from fastapi import FastAPI, Depends
from utils.protected_route import authenticate
from routers import userRoute, questionnaireRoute
from db.db_connection import engine, Base
import asyncio

app = FastAPI()

# TDOD: test the questionnaire route properly
# TODO: maybe move the user to a different service
# TODO: maybe the get the user_id from the frontend and add it

# Create tables asynchronously
@app.on_event("startup")
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

app.include_router(userRoute.router, tags=["users"])
app.include_router(questionnaireRoute.router, tags=["questionnaires"])
