from pydantic import BaseModel
from typing import List, Optional


class blogBase(BaseModel):
    title: str
    sub_title: str
    content: Optional[str] = None

class BlogUpdate(BaseModel):
    title: Optional[str] = None
    sub_title: Optional[str] = None
    content: Optional[str] = None


class BlogCreate(blogBase):
    pass


class Blog(blogBase):
    id: int
    owner_id: int


class CreateUserRequest(BaseModel):
    username: str
    password: str


class UserCreate(CreateUserRequest):
    pass


class User(BaseModel):
    id: int
    name: str
    blogs: List[Blog] = []

class UserResponse(BaseModel):
    id: int
    name: str

class Config:
    from_attributes = True





# class Config:
#     from_attributes = True
