from fastapi import FastAPI
from core.db import get_db


async_session = get_db()
app = FastAPI()

#TODO: initilize the databases
#TODO: add firebase auth either in each service or have a shared service
#TODO: add the routes
#TODO: implement the AI recommendation logic


@app.get("/")
def read_root():
    return {"message": "Hello World"}
