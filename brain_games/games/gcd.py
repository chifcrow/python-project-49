# brain_games/games/gcd.py
import random

RULES = 'Find the greatest common divisor of given numbers.'


def generate_question_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    correct_answer = str(find_gcd(num1, num2))
    return question, correct_answer


def find_gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1
