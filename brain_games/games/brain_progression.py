import prompt
from ..game_logic import random_number, wrong_answer, correct
from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def game_process(name):
    user_name = name
    number_step()
    prog_list = number_step()
    # переводим лист в строку разделяя пробелами
    my_string = ' '.join(map(str, prog_list))
    # верный ответ равен случайной цифре из списка
    answer = prog_list[randint(1, len(prog_list) - 1)]
    # показываем строку, заменяя верный ответ двумя точками (..)
    print(f"Question: {my_string.replace(str(answer), '..')}")
    user_answer = prompt.string('Your answer: ')
    if user_answer == str(answer):
        correct()
    else:
        wrong_answer(user_answer, answer, user_name)


def number_step():
    start = random_number()
    step = randint(2, 5)
    list_prog = list(range(start, 35, step))
    return (list_prog)
