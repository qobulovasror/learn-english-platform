from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import get_db

from services.user_service import get_user_by_userId, get_all_users_from_db, create_user, update_user
from schemas.user import UserCreate
from schemas.user import UserOut
router = APIRouter()

# get user by user id
# @router.get("/users/{user_id}", response_model=UserOut, dependencies=[Depends(get_current_user)])
@router.get("/users/{user_id}", response_model=UserOut)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await get_user_by_userId(user_id, db)
    return user
    

#get all users
@router.get("/users", response_model=list[UserOut])
async def get_all_users(db: AsyncSession = Depends(get_db)):
    users = await get_all_users_from_db(db)
    return users

# create user
@router.post("/users", response_model=UserOut)
async def create_user_api_endpoint(user: UserCreate, db: AsyncSession = Depends(get_db)):
    new_user = await create_user(user, db)
    return new_user

# update user
@router.put("/users/{user_id}", response_model=UserOut)
async def update_user_api_endpoint(user_id: int, user: UserCreate, db: AsyncSession = Depends(get_db)):
    updated_user = await update_user(user_id, user, db)
    return updated_user