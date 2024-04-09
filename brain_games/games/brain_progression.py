from random import randint

DESCRIPTION = 'What number is missing in the progression?'

LOWER_LIMIT = 2
START_UPPER_LIMIT = 10
STEP_UPPER_LIMIT = 5
LIST_UPPER_LIMIT = 35
LOWER_INDEX = 0


def question_and_answer():
    initial_term, common_difference = get_random_numbers()
    finite_arithmetic_progression = LIST_UPPER_LIMIT
    prog_list = get_arithmetic_progression(
        initial_term, finite_arithmetic_progression, common_difference)
    index = randint(LOWER_INDEX, len(prog_list) - 1)  # Индекс скрываемого числа
    answer = prog_list[index]
    question = get_question(prog_list, index)
    return question, answer


def get_question(prog_list, index):
    """Построение строки вопроса"""
    prog_list[index] = '..'
    return ' '.join(map(str, prog_list))


def get_random_numbers():
    """Генерация случайных чисел"""
    start = randint(LOWER_LIMIT, START_UPPER_LIMIT)
    step = randint(LOWER_LIMIT, STEP_UPPER_LIMIT)
    return start, step


def get_arithmetic_progression(start, stop, step):
    """Вычисление членов прогрессии"""
    return list(range(start, stop, step))
