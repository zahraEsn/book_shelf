from typing import Optional, Literal
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    first_name: str
    last_name: str
    phone: str
    email: EmailStr
    role: Literal["admin", "customer", "author"]

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: Optional[str]

class User(UserBase):
    id: Optional[int]