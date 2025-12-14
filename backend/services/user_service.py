from models.user import User
from schemas.user import UserCreate
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from sqlalchemy import select
import logging
logger = logging.getLogger(__name__)

# get user by user id
async def get_user_by_userId(user_id: int, db: AsyncSession) -> User | None:
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        logger.error(f"User not found with ID: {user_id}")
        raise HTTPException(status_code=404, detail="User not found")
    return user

# get all users
async def get_all_users_from_db(db: AsyncSession) -> list[User]:
    result = await db.execute(select(User))
    users = result.scalars().all()
    return users

# create user
async def create_user(user: UserCreate, db: AsyncSession) -> User:
    new_user = User(**user.model_dump())
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

# update user
async def update_user(user_id: int, user: UserCreate, db: AsyncSession) -> User:
    user_to_update = await get_user_by_userId(user_id, db)
    if not user_to_update:
        raise HTTPException(status_code=404, detail="User not found")
    user_to_update.name = user.name
    user_to_update.role = user.role
    user_to_update.info = user.info
    await db.commit()
    await db.refresh(user_to_update)
    return user_to_update