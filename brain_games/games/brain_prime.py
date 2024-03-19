import prompt
from ..cli import welcome_user
from ..game_logic import random_number, wrong_answer, welcome, win_game


def prime_game():
    welcome()
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i < 3:
        game_process(name)
        i += 1
    if i == 3:
        win_game(name)


def game_process(name):
    user_name = name
    num_one = random_number()
    if is_prime(num_one) is True:
        answer = 'yes'
    else:
        answer = 'no'
    print(f'Question: {num_one}')
    user_answer = prompt.string('Your answer: ')
    if user_answer == str(answer):
        print('Correct!')
    else:
        wrong_answer(user_answer, answer, user_name)


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
