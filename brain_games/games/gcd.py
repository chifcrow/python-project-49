# brain_games/games/gcd.py
import random

RULES = 'Find the greatest common divisor of given numbers.'

MIN_NUMBER = 1
MAX_NUMBER = 100


def generate_question_answer():
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = f'What is the greatest common divisor of {num1} and {num2}?'
    correct_answer = str(find_gcd(num1, num2))
    return question, correct_answer


def find_gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1
