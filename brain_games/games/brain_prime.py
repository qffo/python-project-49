from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

LOWER_LIMIT = 2
UPPER_LIMIT = 10


def question_and_answer():
    num = randint(LOWER_LIMIT, UPPER_LIMIT)
    if is_prime(num) is True:
        answer = 'yes'
    else:
        answer = 'no'
    question = num
    return question, answer


def is_prime(number):
    """Определение простого числа"""
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
