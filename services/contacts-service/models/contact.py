from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class ContactRequest(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    subject: str = Field(..., min_length=3, max_length=100)
    message: str = Field(..., min_length=10, max_length=1000)
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
