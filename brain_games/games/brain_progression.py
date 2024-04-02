from random import randint

DESCRIPTION = 'What number is missing in the progression?'

LOWER_LIMIT = 2
START_UPPER_LIMIT = 10
STEP_UPPER_LIMIT = 5
LIST_UPPER_LIMIT = 35


def question_and_answer():
    start, step = get_random_numbers()
    prog_list = number_step(start, step)
    answer = prog_list[randint(1, len(prog_list) - 1)]
    question = get_question(prog_list, answer)
    return question, answer


def get_question(prog_list, answer):
    """Построение строки вопроса"""
    question_str = ' '.join(map(str, prog_list))
    question = f"{question_str.replace(str(answer), '…')}"
    return question


def get_random_numbers():
    """Генерация случайных чисел"""
    start = randint(LOWER_LIMIT, START_UPPER_LIMIT)
    step = randint(LOWER_LIMIT, STEP_UPPER_LIMIT)
    return start, step


def number_step(start, step):
    """Вычисление членов прогрессии"""
    list_prog = list(range(start, LIST_UPPER_LIMIT, step))
    return list_prog
