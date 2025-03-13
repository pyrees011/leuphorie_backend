from fastapi import FastAPI
from routes.settings import router as settings_router  # Ensure correct import
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Settings Service API")

# Allow frontend to make API requests
origins = [
    "http://localhost",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Register the settings router
app.include_router(settings_router, prefix="/api/v1", tags=["settings"])
