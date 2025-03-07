from pydantic import BaseModel, EmailStr
from typing import Optional , List

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None
    
    
class PostCreate(BaseModel):
    main_content: str
    image: Optional[str] = None

class PostResponse(BaseModel):
    id: int
    main_content: str
    image: Optional[str]
    upvotes: int
    downvotes: int
    user_id: int

    class Config:
        orm_mode = True
        
        
class CollabPostCreate(BaseModel):
    project_name: str
    description: str
    skills_required: List[str]

class CollabPostResponse(CollabPostCreate):
    id: int
    user_id: int

    class Config:
        orm_mode = True

class UserProfileCreate(BaseModel):
    name: str
    bio: Optional[str] = None
    skills: List[str]

class UserProfileResponse(UserProfileCreate):
    id: int
    email: str
    profile_picture: Optional[str] = None

    class Config:
        orm_mode = True

class UserProfileUpdate(BaseModel):
    name: Optional[str] = None
    bio: Optional[str] = None
    skills: Optional[List[str]] = None