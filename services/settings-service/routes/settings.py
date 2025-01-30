from fastapi import APIRouter, HTTPException
from models.user_settings import UserSettings, ProfileSettings, NotificationSettings, PreferenceSettings
from core.db import user_settings_collection
from pydantic import BaseModel

router = APIRouter()

# ✅ Define request body model
class CreateUserSettingsRequest(BaseModel):
    username: str
    email: str

# fetch User Settings
@router.get("/settings/{user_id}", response_model=UserSettings)
async def get_user_settings(user_id: str):
    settings = await user_settings_collection.find_one({"user_id": user_id})
    if not settings:
        raise HTTPException(status_code=404, detail="User settings not found")
    return settings

# update Profile Settings
@router.put("/settings/{user_id}/profile")
async def update_profile_settings(user_id: str, profile: ProfileSettings):
    result = await user_settings_collection.update_one(
        {"user_id": user_id}, {"$set": {"profile": profile.dict()}}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User settings not found")
    return {"message": "Profile updated successfully"}

# update Notification Settings
@router.put("/settings/{user_id}/notifications")
async def update_notification_settings(user_id: str, notifications: NotificationSettings):
    result = await user_settings_collection.update_one(
        {"user_id": user_id}, {"$set": {"notifications": notifications.dict()}}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User settings not found")
    return {"message": "Notification settings updated successfully"}

# update Preference Settings
@router.put("/settings/{user_id}/preferences")
async def update_preference_settings(user_id: str, preferences: PreferenceSettings):
    result = await user_settings_collection.update_one(
        {"user_id": user_id}, {"$set": {"preferences": preferences.dict()}}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User settings not found")
    return {"message": "Preference settings updated successfully"}

# reset User Settings
@router.delete("/settings/{user_id}/reset")
async def reset_user_settings(user_id: str):
    default_settings = UserSettings(user_id=user_id, profile=ProfileSettings(), notifications=NotificationSettings(), preferences=PreferenceSettings())
    result = await user_settings_collection.replace_one({"user_id": user_id}, default_settings.dict(), upsert=True)
    return {"message": "User settings reset to default"}

# create test user
@router.post("/settings/{user_id}", response_model=UserSettings)
async def create_user_settings(user_id: str, user_data: CreateUserSettingsRequest):
    """
    Creates a new user settings document with default values, including username and email.
    """
    existing_user = await user_settings_collection.find_one({"user_id": user_id})
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    # ✅ Save username and email from frontend request
    default_settings = {
        "user_id": user_id,
        "profile": {
            "full_name": "",
            "username": user_data.username,
            "email": user_data.email,
            "phone_number": "",
            "bio": "Write a short bio about yourself..."
        },
        "notifications": {
            "email_updates": True,
            "task_reminders": True,
            "newsletter": True,
            "push_task_reminders": False,
            "health_alerts": False,
            "achievements": True
        },
        "preferences": {
            "dark_mode": False,
            "compact_mode": False,
            "language": "English",
            "timezone": "Pacific Time (PT)"
        }
    }

    await user_settings_collection.insert_one(default_settings)
    return default_settings