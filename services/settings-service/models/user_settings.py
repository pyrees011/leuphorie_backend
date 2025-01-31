from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class ProfileSettings(BaseModel):
    full_name: str = ""
    username: str
    email: str
    phone_number: str = ""
    bio: str = "Write a short bio about yourself..."

class NotificationSettings(BaseModel):
    email_updates: bool = True
    task_reminders: bool = True
    newsletter: bool = True
    push_task_reminders: bool = False
    health_alerts: bool = False
    achievements: bool = True

class PreferenceSettings(BaseModel):
    dark_mode: bool = False
    compact_mode: bool = False
    language: str = "English"
    timezone: str = "Pacific Time (PT)"

class UserSettings(BaseModel):
    user_id: str
    profile: ProfileSettings
    notifications: NotificationSettings
    preferences: PreferenceSettings
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
