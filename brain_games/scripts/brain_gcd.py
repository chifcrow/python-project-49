import random
from math import gcd
from brain_games.engine import run_game


def generate_question_and_answer():
    print('Find the greatest common divisor of given numbers.')
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    question = f"{number1} {number2}"
    correct_answer = str(gcd(number1, number2))
    return question, correct_answer


def main():
    run_game(generate_question_and_answer)


if __name__ == "__main__":
    main()
