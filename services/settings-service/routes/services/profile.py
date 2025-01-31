from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from core.db import settings_collection

router = APIRouter()

# Data validation schema for user settings
class UserSettings(BaseModel):
    full_name: str
    username: str
    email: EmailStr
    phone: str
    bio: str
    notifications: dict
    preferences: dict

# Schema for profile updates
class ProfileUpdate(BaseModel):
    full_name: str
    username: str
    email: EmailStr
    phone: str
    bio: str

# ✅ POST: Create User Settings
@router.post("/{user_id}")
async def create_user_settings(user_id: str, user_data: UserSettings):
    existing_user = await settings_collection.find_one({"user_id": user_id})
    
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = {
        "user_id": user_id,
        "full_name": user_data.full_name,
        "username": user_data.username,
        "email": user_data.email,
        "phone": user_data.phone,
        "bio": user_data.bio,
        "notifications": user_data.notifications,
        "preferences": user_data.preferences,
    }

    await settings_collection.insert_one(new_user)
    return {"message": "User created successfully", "user_id": user_id}

# ✅ PUT: Update Profile Settings
@router.put("/{user_id}/profile")
async def update_profile_settings(user_id: str, profile_data: ProfileUpdate):
    existing_user = await settings_collection.find_one({"user_id": user_id})
    
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")

    update_data = {
        "full_name": profile_data.full_name,
        "username": profile_data.username,
        "email": profile_data.email,
        "phone": profile_data.phone,
        "bio": profile_data.bio,
    }

    await settings_collection.update_one({"user_id": user_id}, {"$set": update_data})
    return {"message": "Profile updated successfully"}
