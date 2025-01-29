from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

client = AsyncIOMotorClient(settings.mongodb_uri)
database = client["contact_service_db"]
contact_collection = database["contacts"]
