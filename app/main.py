from fastapi import FastAPI,status, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, crud, schema
from app.database import SessionLocal, engine

from typing import Annotated
from . import auth
from .auth import get_current_user


models.Base.metadata.create_all(bind=engine)

from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
app.include_router(auth.router)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Vue frontend URL ထည့်လို့ရတယ်
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
    
db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@app.get("/")
async def user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"User": user}

@app.get("/blogs/{user_id}", response_model=list[schema.Blog])
def read_blogs(user_id: int, db: db_dependency):
    return crud.get_blog(db=db, user_id = user_id)


@app.post("/blogs/user/{user_id}", response_model=schema.blogBase)
def create_blog_for_user(user_id: int, blog: schema.BlogCreate, db: db_dependency):
    return crud.create_blog(db=db, blog=blog, user_id=user_id)

@app.get("/blogs/title/{title}", response_model=schema.blogBase)
def read_blog_by_title(title: str, db: Session = Depends(get_db)):
    blog = crud.get_blog_by_title(db=db, title=title)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog

@app.get("/users", response_model=list[schema.User])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users


@app.put("/blogs/{blog_id}", response_model=schema.Blog)
def update_blog(blog_id: int, blog_data: schema.BlogUpdate, db: Session = Depends(get_db)):
    return crud.update_blog(db=db, blog_id=blog_id, blog_data=blog_data)



@app.delete("/blogs/{blog_id}", response_model=schema.blogBase)
def delete_blog(blog_id: int, db: db_dependency):
     crud.delete_blog(db=db, blog_id=blog_id)
     return {"detail": "Blog deleted successfully"}
     


