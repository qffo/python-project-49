import prompt
from ..cli import welcome_user
from ..game_logic import random_number, wrong_answer, welcome, win_game


def calc_game():
    welcome()
    name = welcome_user()
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        game_process(name)
        i += 1
    if i == 3:
        win_game(name)


def game_process(name):
    user_name = name
    num_one = random_number()
    num_two = random_number()
    answer = num_one + num_two
    print(f'Question: {num_one} + {num_two}')
    user_answer = prompt.string('Your answer: ')
    if user_answer == str(answer):
        print('Correct!')
    else:
        wrong_answer(user_answer, answer, user_name)
