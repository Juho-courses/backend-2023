from fastapi import FastAPI
from .routers import books, authors

app = FastAPI()

app.include_router(books.router)
app.include_router(authors.router)
