# brain_games/games/calc.py
import random
import operator

RULES = "What is the result of the expression?"

MIN_NUMBER = 1
MAX_NUMBER = 20


def generate_question_answer():
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    op_symbol, operation = random.choice(list(operators.items()))

    question = f"{num1} {op_symbol} {num2}"
    correct_answer = str(operation(num1, num2))
    return question, correct_answer
