from random import randint
import prompt
import sys


def game_logic(games):
    print('Welcome to the brain games!')
    name = prompt.string('May i have your name ? ')
    print(f'Hello, {name}!\n{games.DESCRIPTION}')
    i = 0
    while i < 3:
        question, answer = games.game_question()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == str(answer):
            print('Correct!')
        else:
            wrong_answer(user_answer, answer, name)
        i += 1
    if i == 3:
        print(f"Congratulations, {name}!")


def random_number():
    num = randint(2, 10)
    return num


def wrong_answer(usr_ans, ans, name):
    return print(f"""'{usr_ans}' is wrong answer ;(. Correct answer was '{ans}'.
Let's try again, {name}!"""), sys.exit()
