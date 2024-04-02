from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'

LOWER_LIMIT = 4
UPPER_LIMIT = 20


def question_and_answer():
    num_one, num_two = get_random_numbers()
    question = F"{num_one} {num_two}"
    answer = is_nod(num_one, num_two)
    return question, answer


def get_random_numbers():
    """Генерация случайных чисел"""
    num_one = randint(LOWER_LIMIT, UPPER_LIMIT)
    num_two = randint(LOWER_LIMIT, UPPER_LIMIT)
    return num_one, num_two


def is_nod(num_one, num_two):
    """Определение наибольшего общего делителя (GCD)"""
    while num_two > 0:
        num_one, num_two = num_two, num_one % num_two
    return num_one
# Функция находит наибольший общий делитель двух чисел.
# Она использует алгоритм Евклида, который заключается в последовательном
# нахождении остатка от деления одного числа на другое, затем это число
# становится делимым, а остаток делимым.
# Функция продолжает цикл до тех пор, пока num_two > 0.
# После завершения цикла возвращает num_one, который и будет
# наибольшим общим делителем исходных чисел num_one и num_two.
