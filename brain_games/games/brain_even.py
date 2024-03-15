import prompt
from ..cli import welcome_user
from ..game_logic import random_number, wrong_answer, welcome, win_game


def even_game():
    welcome()
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        game_process(name)
        i += 1
    if i == 3:
        win_game(name)


def game_process(name):
    num = random_number()
    print(f'Question: {num}')
    user_answer = prompt.string('Your answer: ')
    if num % 2 == 0:
        if num % 2 == 0 and user_answer == 'yes':
            print('Correct!')
        else:
            wrong_answer(user_answer, 'yes', name)
    if num % 2 != 0:
        if num % 2 != 0 and user_answer == 'no':
            print('Correct!')
        else:
            wrong_answer(user_answer, 'no', name)
