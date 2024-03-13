# brain_games/engine.py
import prompt


def run_game(game_module):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    correct_answers = 0
    while correct_answers < 3:
        question, correct_answer = game_module.generate_question_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')# brain_games/engine.py


if __name__ == '__main__':
    import brain_games.games.even as game_module
    run_game(game_module)
