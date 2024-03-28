from ..game_logic import random_number
from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def game_question():
    prog_list = number_step()
    my_string = ' '.join(map(str, prog_list))
    answer = prog_list[randint(1, len(prog_list) - 1)]
    question = f"{my_string.replace(str(answer), '..')}"
    return question, answer


def number_step():
    """Поиск пропущенных чисел в последовательности чисел"""
    start = random_number()
    step = randint(2, 5)
    list_prog = list(range(start, 35, step))
    return (list_prog)
