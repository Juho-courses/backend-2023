from sqlalchemy.orm import Session
from . import models, schemas


def read_numbers(db: Session):
    return db.query(models.Number).all()


def create_number(db: Session, number_in: schemas.NumberIn):
    number = models.Number(**number_in.dict())
    db.add(number)
    db.commit()
    db.refresh(number)
    return number
