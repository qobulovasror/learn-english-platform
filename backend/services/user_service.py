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
async def update_user(user_to_update: User, user: UserCreate, db: AsyncSession) -> User:
    user_to_update.name = user.name
    user_to_update.role = user.role
    user_to_update.info = user.info
    user_to_update.birth_date = user.birth_date
    user_to_update.phone_number = user.phone_number
    user_to_update.address = user.address
    user_to_update.gender = user.gender
    user_to_update.email = user.email
    await db.commit()
    await db.refresh(user_to_update)
    return user_to_update

# delete user
async def delete_user(user_to_delete: User, db: AsyncSession) -> bool:
    await db.delete(user_to_delete)
    await db.commit()
    return True