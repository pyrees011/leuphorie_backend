from typing import Optional
from pydantic import BaseModel, EmailStr

class ProfileSettings(BaseModel):
    full_name: str
    username: str
    email: EmailStr
    phone_number: str
    bio: Optional[str] = "Write a short bio about yourself..."
    profile_picture: str = "https://example.com/avatar-placeholder.png"  # Placeholder URL

class NotificationSettings(BaseModel):
    email_updates: bool = True
    email_reminders: bool = True
    email_newsletter: bool = False
    push_reminders: bool = True
    push_health_alerts: bool = True
    push_achievements: bool = True

class PreferenceSettings(BaseModel):
    dark_mode: bool = False
    compact_mode: bool = False
    language: str = "English"
    time_zone: str = "Pacific Time (PT)"

class UserSettings(BaseModel):
    user_id: str
    profile: ProfileSettings
    notifications: NotificationSettings
    preferences: PreferenceSettings
