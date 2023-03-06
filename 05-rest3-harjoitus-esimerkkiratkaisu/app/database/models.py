from pydantic import BaseModel


class AuthorBase(BaseModel):
    name: str


class AuthorDb(AuthorBase):
    id: int


class BookIn(BaseModel):
    title: str
    author: str


class BookDb(BookIn):
    id: int
