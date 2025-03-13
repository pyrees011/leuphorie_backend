from pydantic import BaseModel, ConfigDict
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
