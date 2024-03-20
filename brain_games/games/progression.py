# brain_games/games/progression.py
import random

PROGRESSION_LENGTH = 10
START_MIN = 1
START_MAX = 10
STEP_MIN = 1
STEP_MAX = 10

RULES = 'What number is missing in the progression?'


def generate_question_answer():
    progression_length = 10
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    missing_index = random.randint(0, progression_length - 1)

    progression = [str(start + step * i) for i in range(progression_length)]
    correct_answer = progression[missing_index]
    progression[missing_index] = '..'
    question = ' '.join(progression)

    return question, correct_answer
