# brain_games/games/calc.py
import random
import operator


def generate_question_answer():
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    op_symbol, operation = random.choice(list(operators.items()))

    question = f"{num1} {op_symbol} {num2}"
    correct_answer = str(operation(num1, num2))

    print("What is the result of the expression?")  # Выводим запрос задачи
    return question, correct_answer
