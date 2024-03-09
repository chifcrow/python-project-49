# brain_games/games/gcd.py
import random
import math

def generate_question_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f'{num1} {num2}'
    answer = str(math.gcd(num1, num2))
    return question, answer