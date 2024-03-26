import prompt
from ..game_logic import random_number, wrong_answer

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def game_process(name):
    user_name = name
    num_one = random_number() * 2
    num_two = random_number() * 2
    answer = nod(num_one, num_two)
    print(f'Question: {num_one} {num_two}')
    user_answer = prompt.string('Your answer: ')
    if user_answer == str(answer):
        print('Correct!')
    else:
        wrong_answer(user_answer, answer, user_name)


def nod(num_one, num_two):
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
