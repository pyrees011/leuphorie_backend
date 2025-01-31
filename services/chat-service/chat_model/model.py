from openai import AsyncOpenAI
import os
from dotenv import load_dotenv
from models.chat import ChatSession
from datetime import datetime
from bson import ObjectId
from db.mongo import chat_collection

load_dotenv()

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def generate_response(messages):
    try:
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=500,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating response: {e}")
        return "I apologize, but I'm having trouble generating a response right now."

async def get_or_create_session(session_id: str = None, user_id: str = None):
    """
    Retrieves an existing chat session or creates a new one if it doesn't exist.

    :param session_id: Optional session identifier
    :param user_id: Optional user ID (for authenticated users)
    :return: ChatSession object
    """
    if session_id:
        session = await chat_collection.find_one({"session_id": session_id})
        if session:
            return ChatSession(**session)

    # Create a new chat session
    new_session = ChatSession(
        session_id=str(ObjectId()),
        user_id=user_id,
        conversation=[],
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    await chat_collection.update_one(
        {"session_id": new_session.session_id},
        {"$setOnInsert": new_session.model_dump(by_alias=True)},
        upsert=True
    )

    return new_session