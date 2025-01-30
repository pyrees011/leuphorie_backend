from fastapi import APIRouter, Depends, HTTPException
from typing import List
from services.chat_service import process_chat_message
from utils.protected_route import authenticate
from models.chat import ChatRequest
router = APIRouter()

@router.post("/chat", dependencies=[Depends(authenticate)])
async def chat_endpoint(chat_request: ChatRequest):
    try:
        response = await process_chat_message(chat_request.message, chat_request.conversation_history)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))