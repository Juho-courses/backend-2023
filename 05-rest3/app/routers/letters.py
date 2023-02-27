from fastapi import APIRouter
from app.database.models import LetterDB
from ..database.database import letters

router = APIRouter(prefix='/letters')


@router.get('', response_model=list[LetterDB])
def get_letters():
    return letters
