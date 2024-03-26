import prompt
from ..game_logic import random_number, wrong_answer

DESCRIPTION = 'What is the result of the expression?'


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
