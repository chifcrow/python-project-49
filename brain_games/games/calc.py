# brain_games/games/calc.py
import random
import operator

def generate_question_answer():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operation, func = random.choice(list({'+' : operator.add, '-' : operator.sub, '*' : operator.mul}.items()))
    question = f'{num1} {operation} {num2}'
    answer = str(func(num1, num2))
    return question, answer