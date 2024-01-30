# brain_games/games/calculator.py


import random
import operator


def generate_question_and_answer():
    print('What is the result of the expression?')
    # Генерация двух случайных чисел
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)

    # Выбор случайной операции
    operations = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    operation_symbol, operation = random.choice(list(operations.items()))

    # Формирование вопроса и расчет правильного ответа
    question = f"{num1} {operation_symbol} {num2}"
    correct_answer = operation(num1, num2)

    return question, str(correct_answer)  # Преобразование ответа в строку
