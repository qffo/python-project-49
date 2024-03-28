from ..game_logic import random_number
from random import choice

DESCRIPTION = 'What is the result of the expression?'


def game_question():
    """Калькулятор"""
    num_one = random_number()
    num_two = random_number()
    operations = choice(['+', '-', '*'])
    if operations == '+':
        answer = num_one + num_two
    if operations == '-':
        answer = num_one - num_two
    if operations == '*':
        answer = num_one * num_two
    question = f"{num_one} {operations} {num_two}"
    return question, answer
