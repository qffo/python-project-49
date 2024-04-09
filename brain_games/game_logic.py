import prompt
import sys

ROUNDS_QTY = 3


def play_game(game):
    print('Welcome to the brain games!')
    name = prompt.string('May i have your name ? ')
    print(f'Hello, {name}!\n{game.DESCRIPTION}')
    i = 0
    while i < ROUNDS_QTY:
        question, ans = game.question_and_answer()
        print(f'Question: {question}')
        user_ans = prompt.string('Your answer: ')
        if user_ans == str(ans):
            print('Correct!')
        else:
            print(
                f"""'{user_ans}' is wrong answer ;(. Correct answer was '{ans}'.
Let's try again, {name}!"""), sys.exit()
        i += 1
    if i == ROUNDS_QTY:
        print(f"Congratulations, {name}!")
