from fastapi import FastAPI
from routes.contact import router as contact_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Contact Service API", version="1.0.0")


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


# Include routes
app.include_router(contact_router, prefix="/contact-requests", tags=["Contact Requests"])
