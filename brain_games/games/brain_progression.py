import prompt
from ..cli import welcome_user
from ..game_logic import random_number, wrong_answer, welcome, win_game
from random import choice


def progression_game():
    welcome()
    name = welcome_user()
    print('What number is missing in the progression?')
    i = 0
    while i < 3:
        game_process(name)
        i += 1
    if i == 3:
        win_game(name)


def game_process(name):
    user_name = name
    number_step()
    prog_list = number_step()
    # переводим лист в строку разделяя пробелами
    my_string = ' '.join(map(str, prog_list))
    # верный ответ равен случайной цифре из списка
    answer = choice(prog_list)
    # показываем строку, заменяя верный ответ тремя точками (...)
    print(f"Question: {my_string.replace(str(answer), '...')}")
    user_answer = prompt.string('Your answer: ')
    if user_answer == str(answer):
        print('Correct!')
    else:
        wrong_answer(user_answer, answer, user_name)


def number_step():
    start = random_number()
    step = random_number()
    list_prog = []
    element = start
    while len(list_prog) < 10:
        list_prog.append(element)
        element += step
    return (list_prog)
