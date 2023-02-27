from .models import NumberDb


numbers = [
    {'id': 0, 'number': 123},
    {'id': 1, 'number': 1231},
    {'id': 2, 'number': 123192},
]

letters = [
    {'id': 0, 'letter': 'a'},
    {'id': 1, 'letter': 'b'},
]


def save_number(number_in):
    new_id = len(numbers)
    number = NumberDb(**number_in.dict(), id=new_id)
    numbers.append(number.dict())
    return number
