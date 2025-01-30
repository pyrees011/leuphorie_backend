from pydantic import BaseModel
from typing import Optional, List, Dict

# Define a Pydantic model for the request body
class ChatRequest(BaseModel):
    message: str
    conversation_history: Optional[List[Dict[str, str]]] = []