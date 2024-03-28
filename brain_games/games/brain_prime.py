from ..game_logic import random_number

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_question():
    num_one = random_number()
    if is_prime(num_one) is True:
        answer = 'yes'
    else:
        answer = 'no'
    question = num_one
    return question, answer


def is_prime(number):
    """Определение простого числа"""
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
