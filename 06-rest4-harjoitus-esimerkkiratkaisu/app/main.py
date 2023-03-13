from fastapi import FastAPI
from .routers import books, authors

from .database import models
from .database.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(books.router)
app.include_router(authors.router)
