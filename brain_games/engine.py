# brain_games/engine.py
import prompt

def run_game(game_module):
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    for _ in range(3):
        question, correct_answer = game_module.generate_question_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')