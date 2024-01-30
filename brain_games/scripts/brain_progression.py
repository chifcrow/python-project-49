import random
from brain_games.engine import run_game


def generate_progression_and_question():
    print('What number is missing in the progression?')
    progression_length = random.randint(5, 10)
    start = random.randint(1, 20)
    step = random.randint(1, 5)
    hidden_index = random.randint(0, progression_length - 1)

    progression = [str(start + step * i) for i in range(progression_length)]
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."
    question = ' '.join(progression)

    return question, correct_answer


def main():
    run_game(generate_progression_and_question)


if __name__ == '__main__':
    main()
