from fastapi import FastAPI
from routers import task_router


app = FastAPI()

#TODO: initilize the databases
#TODO: clean up the code
#TODO: add the routes
#TODO: implement the AI recommendation logic

app.include_router(task_router.router, tags=["tasks"])


@app.get("/")
def read_root():
    return {"message": "Task Service API"}