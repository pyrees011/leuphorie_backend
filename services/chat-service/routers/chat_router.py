from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Optional
from services.chat_service import process_chat_message, get_conversation_history as get_conversation_history_service
from utils.protected_route import authenticate
from models.chat import ChatMessage, ChatResponse

router = APIRouter()

@router.post("/chat/{user_id}", response_model=ChatResponse, dependencies=[Depends(authenticate)])
async def chat_endpoint(
    user_id: str,
    chat_message: ChatMessage
):
    try:
        response = await process_chat_message(
            message=chat_message.message,
            user_id=user_id,
            session_id=chat_message.session_id
        )
        return response
    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/chat/{user_id}", dependencies=[Depends(authenticate)])
async def get_conversation_history(
    user_id: str,
    session_id: Optional[str] = Query(None)
):
    if session_id:
        return await get_conversation_history_service(session_id, user_id)
    else:
        return []