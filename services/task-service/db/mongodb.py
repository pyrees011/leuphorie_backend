from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")

# MongoDB client
client = AsyncIOMotorClient(MONGODB_URL)
database = client.task_management
task_collection = database.tasks 