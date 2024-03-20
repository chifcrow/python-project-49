# brain_games/games/even.py
import random

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'

def is_even(number):
    return number % 2 == 0

MIN_NUMBER = 1
MAX_NUMBER = 100

def generate_question_answer():
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, correct_answer
