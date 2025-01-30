from chat_model.model import generate_response
from datetime import datetime
from typing import Optional
from db.mongo import chat_collection
from chat_model.model import get_or_create_session

async def process_chat_message(message: str, user_id: str, session_id: Optional[str] = None):
    session = await get_or_create_session(session_id, user_id)
    messages = []

    if not session.conversation:
        # Format the conversation history for OpenAI
        system_message = {
            "role": "system", 
            "content": "You are a helpful mental health assistant, focused on providing support and guidance while maintaining appropriate boundaries and encouraging professional help when needed."
        }
        messages.append(system_message)
    else:
        # Add conversation history
        for msg in session.conversation:
            if isinstance(msg, list):  # Handle the case where msg is a list
                messages.extend(msg)
            else:
                role = "assistant" if msg.get("is_bot") else "user"
                messages.append({"role": role, "content": msg.get("content", "")})
    
    # Add the new user message
    messages.append({"role": "user", "content": message})
    
    # Generate response
    response = await generate_response(messages)
    # response = "Hello"

    # Update conversation in database
    await chat_collection.update_one(
        {"session_id": session.session_id},
        {
            "$push": {
                "conversation": {
                    "$each": [
                        {"role": "user", "content": message, "is_bot": False},
                        {"role": "assistant", "content": response, "is_bot": True}
                    ]
                }
            },
            "$set": {"updated_at": datetime.utcnow()}
        },
        upsert=True
    )
    
    return {
        "session_id": session.session_id,
        "content": response,
        "timestamp": datetime.utcnow(),
        "is_bot": True
    }

async def get_conversation_history(session_id: str, user_id: str):
    conversation = await chat_collection.find_one({"session_id": session_id, "user_id": user_id})
    return conversation.get("conversation", []) if conversation else []