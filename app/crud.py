from sqlalchemy.orm import Session
from app import models, schema

def get_user(db: Session):
    return db.query(models.User).all()

def get_blog(db: Session):
    return db.query(models.Blog).all()

# def create_user(db: Session, user: user_schema.UserCreate):
#     db_user = models.User(name=user.name, password=user.password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# def get_user_by_id(db: Session, user_id: int):
#     db_user = db.query(models.User).filter(models.User.id == user_id)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


def create_blog(db: Session, blog: schema.BlogCreate, user_id: int):
    db_blog = models.Blog(**blog.dict(), owner_id=user_id)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog
