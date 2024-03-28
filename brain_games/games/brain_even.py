import prompt
from ..game_logic import random_number, wrong_answer, correct

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_process(name):
    num = random_number()
    print(f'Question: {num}')
    user_answer = prompt.string('Your answer: ')
    if num % 2 == 0:
        if num % 2 == 0 and user_answer == 'yes':
            correct()
        else:
            wrong_answer(user_answer, 'yes', name)
    if num % 2 != 0:
        if num % 2 != 0 and user_answer == 'no':
            correct()
        else:
            wrong_answer(user_answer, 'no', name)
