from pydantic import BaseModel, EmailStr
from typing import Optional, Dict, Any

class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str]

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    profile: Optional[Dict[str, Any]]

    class Config:
        orm_mode = True
