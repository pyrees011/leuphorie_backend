from fastapi import FastAPI
from routers import task_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

#TODO: initilize the databases
#TODO: clean up the code
#TODO: add the routes
#TODO: implement the AI recommendation logic

origins = [
    "http://localhost:3000",  # Frontend running on React/Next.js
    "http://127.0.0.1:3000",
]

# Enable CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows specified frontend origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, PUT, DELETE, OPTIONS, etc.)
    allow_headers=["*"],  # Allows all headers
)

app.include_router(task_router.router, prefix="/api/v1", tags=["tasks"])


@app.get("/")
def read_root():
    return {"message": "Task Service API"}