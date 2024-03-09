# brain_games/games/progression.py
import random


def generate_question_answer():
    start = random.randint(1, 10)
    step = random.randint(1, 5)
    length = random.randint(5, 10)
    hidden_index = random.randint(0, length - 1)

    progression = [str(start + i * step) for i in range(length)]
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    question = ' '.join(progression)

    return question, correct_answer