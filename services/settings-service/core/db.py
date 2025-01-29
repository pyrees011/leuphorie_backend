import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGODB_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
database = client[DATABASE_NAME]
user_settings_collection = database[COLLECTION_NAME]
