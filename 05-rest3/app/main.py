from fastapi import FastAPI
from .routers import numbers, letters

app = FastAPI()

app.include_router(numbers.router)
app.include_router(letters.router)
