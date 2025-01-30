from fastapi import FastAPI, Depends
from utils.protected_route import authenticate
from routers import userRoute, questionnaireRoute
from db.db_connection import engine, Base
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# TDOD: test the questionnaire route properly
# TODO: maybe move the user to a different service
# TODO: maybe the get the user_id from the frontend and add it

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

# Create tables asynchronously
@app.on_event("startup")
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

app.include_router(userRoute.router, prefix="/api/v1", tags=["users"])
app.include_router(questionnaireRoute.router, prefix="/api/v1", tags=["questionnaires"])
