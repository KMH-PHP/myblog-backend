from sqlalchemy.orm import Session
from app import models, schema
from fastapi import HTTPException

def get_user(db: Session):
    return db.query(models.User.id, models.User.name).all()

def get_blog(db: Session, user_id: int):
    db_blog = db.query(models.Blog).filter(models.Blog.owner_id == user_id).all()
    return db_blog

def get_blog_by_title(db: Session, title: str):
    return db.query(models.Blog).filter(models.Blog.title == title).first()


def create_blog(db: Session, blog: schema.BlogCreate, user_id: int):
    db_blog = models.Blog(**blog.dict(), owner_id=user_id)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog

def update_blog(db: Session, blog_id: int, blog_data: schema.BlogUpdate):
    db_blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()

    if not db_blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    
      # update only the fields that are provided
    update_data = blog_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_blog, key, value)

    db.commit()
    db.refresh(db_blog)
    return db_blog

def delete_blog(db: Session, blog_id: int):
    db_blog = db.query(models.Blog).get(blog_id)

    if not db_blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    
    db.delete(db_blog)
    db.commit()
    return db_blog  


