from chat_model.model import generate_response
from datetime import datetime

async def process_chat_message(user_message: str, conversation_history: list):
    # Format the conversation history for OpenAI
    messages = [
        {"role": "system", "content": "You are a helpful mental health assistant, focused on providing support and guidance while maintaining appropriate boundaries and encouraging professional help when needed."}
    ]
    
    # Add conversation history
    for msg in conversation_history:
        role = "assistant" if msg.get("is_bot") else "user"
        messages.append({"role": role, "content": msg.get("content", "")})
    
    # Add the new user message
    messages.append({"role": "user", "content": user_message})
    
    # Generate response
    response = await generate_response(messages)
    
    return {
        "content": response,
        "timestamp": datetime.utcnow(),
        "is_bot": True
    }