from fastapi import FastAPI
from routes.contact import router as contact_router

app = FastAPI(title="Contact Service API", version="1.0.0")

# Include routes
app.include_router(contact_router, prefix="/contact-requests", tags=["Contact Requests"])
