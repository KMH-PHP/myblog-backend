from fastapi import FastAPI,status, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, crud, schema
from app.database import SessionLocal, engine

from typing import Annotated
from . import auth
from .auth import get_current_user


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth.router)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@app.get("/")
async def user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"User": user}

@app.get("/blogs", response_model=list[schema.blogBase])
def read_blogs(db: db_dependency):
    return crud.get_blog(db=db)

# @app.post("/users", response_model=user_schema.UserBase)
# def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
#     return crud.create_user(db=db, user=user)

@app.post("/blogs/{user_id}", response_model=schema.blogBase)
def create_blog_for_user(user_id: int, blog: schema.BlogCreate, db: db_dependency):
    return crud.create_blog(db=db, blog=blog, user_id=user_id)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Vue frontend URL ထည့်လို့ရတယ်
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

