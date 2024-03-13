# brain_games/games/progression.py
import random


def generate_question_answer():
    print("What number is missing in the progression?")  # Добавляем это уведомление

    progression_length = 10
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    missing_index = random.randint(0, progression_length - 1)

    progression = [str(start + step * i) for i in range(progression_length)]
    correct_answer = progression[missing_index]
    progression[missing_index] = '..'
    question = ' '.join(progression)

    return question, correct_answer
