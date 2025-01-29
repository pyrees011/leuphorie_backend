from fastapi import APIRouter, Depends, HTTPException
from services.userService import get_users as get_users_service, get_user_by_id as get_user_by_id_service, get_user_by_email as get_user_by_email_service, create_user as create_user_service, update_user as update_user_service, delete_user as delete_user_service
from schemas.user_schema import UserResponse, UserCreate
from utils.protected_route import authenticate
from sqlalchemy.ext.asyncio import AsyncSession
from db.db_connection import get_db

router = APIRouter()

@router.get("/users", response_model=list[UserResponse], dependencies=[Depends(authenticate)])
async def get_users(db: AsyncSession = Depends(get_db)):
    return await get_users_service(db)

@router.get("/users/{user_id}", response_model=UserResponse, dependencies=[Depends(authenticate)])
async def get_user_by_id(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await get_user_by_id_service(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/users/email/{email}", response_model=UserResponse, dependencies=[Depends(authenticate)])
async def get_user_by_email(email: str, db: AsyncSession = Depends(get_db)):
    user = await get_user_by_email_service(email, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users", response_model=UserResponse, dependencies=[Depends(authenticate)])
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user_service(user, db)

@router.put("/users/{user_id}", response_model=UserResponse, dependencies=[Depends(authenticate)])
async def update_user(user_id: int, user: UserCreate, db: AsyncSession = Depends(get_db)):
    updated_user = await update_user_service(user_id, user, db)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/users/{user_id}", response_model=UserResponse, dependencies=[Depends(authenticate)])
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    deleted_user = await delete_user_service(user_id, db)
    if not deleted_user:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted_user
