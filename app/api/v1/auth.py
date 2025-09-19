from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserCreate, UserOut
from app.core_utils.security import hash_password, verify_password, create_access_token

router = APIRouter()

@router.post('/register', response_model=UserOut)
async def register(user: UserCreate):
    # stubbed: store user in DB
    hashed = hash_password(user.password)
    return {"id": 1, "email": user.email, "full_name": user.full_name, "profile": {}}

@router.post('/login')
async def login():
    # implement JWT
    return {"access_token": "xyz", "token_type": "bearer"}
