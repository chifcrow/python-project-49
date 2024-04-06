# brain_games/games/progression.py
import random

PROGRESSION_LENGTH = 10
START_MIN = 1
START_MAX = 10
STEP_MIN = 1
STEP_MAX = 10

RULES = 'What number is missing in the progression?'


def generate_question_answer():
    start = random.randint(START_MIN, START_MAX)
    step = random.randint(STEP_MIN, STEP_MAX)
    missing_index = random.randint(0, PROGRESSION_LENGTH - 1)

    progression = [str(start + step * i) for i in range(PROGRESSION_LENGTH)]
    correct_answer = progression[missing_index]
    progression[missing_index] = '..'
    question = ' '.join(progression)

    return question, correct_answer
