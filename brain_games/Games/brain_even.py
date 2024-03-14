#!/usr/bin/env python3

from random import randint
import prompt
from ..cli import welcome_user


def wrong_answer_message(usr_ans, ans, name):
    return print(f"""'{usr_ans}' is wrong answer ;(. Correct answer was '{ans}'.
Let's try again, {name}!""")


def foo():
    pass


def even_game():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        number = randint(1, 10)
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ')
        if number % 2 == 0 and user_answer == 'yes':
            print('Correct!')
        if number % 2 == 0 and user_answer == 'no':
            wrong_answer_message(user_answer, 'yes', name)
            break
        if number % 2 != 0 and user_answer == 'no':
            print('Correct!')
        if number % 2 != 0 and user_answer == 'yes':
            wrong_answer_message(user_answer, 'no', name)
            break
        i += 1
    if i == 3:
        print(f"Congratulations, {name}!")
