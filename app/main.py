#py -3 or -m venv venv
#venv\Scripts\activate.bat
#pip install fastapi[all]
#pip install psycopg2
#uvicorn main:app or app.main:app --reload

from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/") 
def root():
    return {"message": "hello!!!"}

#8:59