from pydantic import BaseModel


class AuthorBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class AuthorDb(AuthorBase):
    id: int


class BookIn(BaseModel):
    title: str
    author: str

    class Config:
        orm_mode = True


class BookDb(BookIn):
    id: int
