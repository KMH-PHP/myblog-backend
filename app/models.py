from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "admin"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    hashed_password = Column(String)

    blogs = relationship("Blog", back_populates="owner") 


class Blog(Base):
    __tablename__ = "blog"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    sub_title = Column(String, index=True)
    content = Column(String)

    owner_id = Column(Integer, ForeignKey("admin.id"))

    owner = relationship("User", back_populates="blogs")