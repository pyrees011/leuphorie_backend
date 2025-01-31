from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGODB_URL")

client = AsyncIOMotorClient(MONGO_URI)
database = client.settings_management
settings_collection = database.settings
