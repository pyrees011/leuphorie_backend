from fastapi import FastAPI, Depends
from utils.protected_route import authenticate
from fastapi.middleware.cors import CORSMiddleware
from routers import chat_router

app = FastAPI()

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


@app.get("/")
def read_root():
    return {"message": "Chat Service is running"}

app.include_router(chat_router.router, prefix="/api/v1", tags=["chat"])