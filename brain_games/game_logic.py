from random import randint
import sys


def random_number():
    num = randint(1, 10)
    return num


def wrong_answer(usr_ans, ans, name):
    return print(f"""'{usr_ans}' is wrong answer ;(. Correct answer was '{ans}'.
Let's try again, {name}!"""), sys.exit()


def welcome():
    print("Welcome to the Brain Games!")


def win_game(name):
    print(f"Congratulations, {name}!")
