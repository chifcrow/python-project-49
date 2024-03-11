# brain_games/games/even.py
import random

def generate_question_answer():
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return question, correct_answer


def main():
    game_name = 'Answer "yes" if the number is even, otherwise answer "no".'
    brain_games.engine.run(generate_question_answer, game_name)
