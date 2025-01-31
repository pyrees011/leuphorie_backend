from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from core.db import settings_collection

router = APIRouter()

# Data validation schema
class PreferenceSettings(BaseModel):
    dark_mode: bool
    compact_mode: bool
    language: str
    timezone: str

@router.put("/{user_id}/preferences")
async def update_preferences(user_id: str, settings: PreferenceSettings):
    result = await settings_collection.update_one(
        {"user_id": user_id},
        {"$set": settings.dict()},
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="User not found or no changes made")
    return {"message": "Preferences updated successfully"}
