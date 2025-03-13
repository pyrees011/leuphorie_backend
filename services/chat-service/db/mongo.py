from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")

# MongoDB client
client = AsyncIOMotorClient(MONGODB_URL)
database = client.chat_management
chat_collection = database.chat
