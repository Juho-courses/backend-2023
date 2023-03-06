from sqlalchemy import Column, Integer

from .database import Base


class Number(Base):
    __tablename__ = 'numbers'

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, nullable=False)
