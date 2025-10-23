from pydantic import BaseModel
from typing import List, Optional

class blogBase(BaseModel):
    title: str
    sub_title: str
    content: Optional[str] = None

class BlogCreate(blogBase):
    pass

class Blog(blogBase):
    id: int
    owner_id: int

    class Config:
        form_attributes = True


class CreateUserRequest(BaseModel):
    username: str
    password: str


class UserCreate(CreateUserRequest):
    pass

class User(CreateUserRequest):
    id: int
    blogs: List[Blog] = []

    class Config:
        form_attributes = True