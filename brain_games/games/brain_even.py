from ..game_logic import random_number

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_question():
    """Определение четного числа"""
    num = random_number()
    question = num
    if num % 2 == 0:
        answer = 'yes'
    if num % 2 != 0:
        answer = 'no'
    return question, answer
