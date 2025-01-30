from datetime import datetime
from typing import List, Dict, Optional
from pydantic import BaseModel, Field
from bson import ObjectId

class ChatMessage(BaseModel):
    message: str
    session_id: Optional[str] = None

class ChatResponse(BaseModel):
    session_id: str
    content: str
    timestamp: datetime
    is_bot: bool

class ChatSession(BaseModel):
    session_id: str
    user_id: Optional[str]
    conversation: List[dict] = []
    created_at: datetime
    updated_at: datetime