from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from core.db import user_settings_collection

router = APIRouter()

# Data validation schema
class NotificationSettings(BaseModel):
    email_updates: bool
    task_reminders: bool
    newsletter: bool
    push_reminders: bool
    health_alerts: bool
    achievements: bool

@router.put("/{user_id}/notifications")
async def update_notifications(user_id: str, settings: NotificationSettings):
    result = await user_settings_collection.update_one(
        {"user_id": user_id},
        {"$set": settings.dict()},
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="User not found or no changes made")
    return {"message": "Notification settings updated successfully"}
