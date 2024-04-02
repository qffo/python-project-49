from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

LOWER_LIMIT = 2
UPPER_LIMIT = 10


def question_and_answer():
    num = randint(LOWER_LIMIT, UPPER_LIMIT)
    if is_even(num) is True:
        answer = 'yes'
    else:
        answer = 'no'
    question = num
    return question, answer


def is_even(number):
    """Определение четного числа"""
    if number % 2 == 0:
        return True
    if number % 2 != 0:
        return False
