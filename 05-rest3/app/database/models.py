from pydantic import BaseModel


class NumberIn(BaseModel):
    number: int


class NumberDb(NumberIn):
    id: int


class LetterBase(BaseModel):
    letter: str


class LetterDB(LetterBase):
    id: int
