from models.user import User
from sqlalchemy import select
from schemas.user_schema import UserResponse, UserCreate
from sqlalchemy.ext.asyncio import AsyncSession

async def get_users(db: AsyncSession):
    result = await db.execute(select(User))
    users = result.scalars().all()
    return [UserResponse.model_validate(user, from_attributes=True) for user in users]

async def get_user_by_id(user_id: int, db: AsyncSession):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    return UserResponse.model_validate(user, from_attributes=True) if user else None

async def get_user_by_email(email: str, db: AsyncSession):
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()
    return UserResponse.model_validate(user, from_attributes=True) if user else None

async def create_user(user_data: UserCreate, db: AsyncSession):
    new_user = User(
        username=user_data.username,
        email=user_data.email
    )
    
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return UserResponse.model_validate(new_user, from_attributes=True)

async def update_user(user_id: int, user_data: UserCreate, db: AsyncSession):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        return None
    
    user.username = user_data.username
    user.email = user_data.email
    
    await db.commit()
    await db.refresh(user)
    return UserResponse.model_validate(user, from_attributes=True)

async def delete_user(user_id: int, db: AsyncSession):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if user:
        await db.delete(user)
        await db.commit()
        return UserResponse.model_validate(user, from_attributes=True)
    return None
