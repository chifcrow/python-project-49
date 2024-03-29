# brain_games/games/even.py
import random

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'

MIN_NUMBER = 1
MAX_NUMBER = 100


def generate_question_answer():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = f"Question: {number}"
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return question, correct_answer
