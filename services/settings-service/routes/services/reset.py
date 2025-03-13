from fastapi import APIRouter, HTTPException
from core.db import settings_collection

router = APIRouter()

@router.delete("/{user_id}/reset")
async def reset_settings(user_id: str):
    result = await settings_collection.delete_one({"user_id": user_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User settings deleted"}
