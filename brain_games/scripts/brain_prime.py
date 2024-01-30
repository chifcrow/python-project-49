# brain_games/games/brain_prime.py

import random
from brain_games.engine import run_game


def is_prime(number):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    """Проверяет, является ли число простым."""
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_question_and_answer():
    """Генерирует вопрос и правильный ответ для игры 'Простое ли число?'."""
    number = random.randint(1, 100)
    question = f"{number}"
    answer = "yes" if is_prime(number) else "no"
    return question, answer


def main():
    """Функция запуска игры 'Простое ли число?'."""
    run_game(generate_question_and_answer)


if __name__ == "__main__":
    main()
