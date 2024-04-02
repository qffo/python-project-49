from random import choice, randint

DESCRIPTION = 'What is the result of the expression?'

LOWER_LIMIT = 2
UPPER_LIMIT = 10


def question_and_answer():
    """Калькулятор"""
    num_one, num_two = get_random_numbers()
    operations = choice(['+', '-', '*'])
    if operations == '+':
        answer = num_one + num_two
    if operations == '-':
        answer = num_one - num_two
    if operations == '*':
        answer = num_one * num_two
    question = f"{num_one} {operations} {num_two}"
    return question, answer


def get_random_numbers():
    """Генерация случайных чисел"""
    num_one = randint(LOWER_LIMIT, UPPER_LIMIT)
    num_two = randint(LOWER_LIMIT, UPPER_LIMIT)
    return num_one, num_two
