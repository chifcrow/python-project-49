# brain_games/engine.py
from prompt_toolkit import prompt

NUM_ROUNDS = 3


def run(game_module):
    print('Welcome to the Brain Games!')
    name = prompt('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_module.RULES)  # Выводим правила игры

    correct_answers = 0
    while correct_answers < NUM_ROUNDS:
        question, correct_answer = game_module.generate_question_answer()
        print(f'Question: {question}')
        user_answer = prompt('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
