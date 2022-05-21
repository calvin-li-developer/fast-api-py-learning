import email
from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime
from pydantic import conint

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    
class UserResponseOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        orm_mode = True
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    created_at: datetime
    user_id: int
    user: UserResponseOut
    
    class Config:
        orm_mode = True
        
class PostOut(BaseModel):
    Post: PostResponse
    votes: int
    
    class Config:
        orm_mode = True
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: Optional[str] = None
    
class Vote(BaseModel):
    post_id: int 
    dir: conint(ge=0, le=1)