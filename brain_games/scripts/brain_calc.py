# brain_games/scripts/brain_calc.py

from brain_games.engine import run_game
from brain_games.games.calculator import generate_question_and_answer


def main():
    run_game(generate_question_and_answer)


if __name__ == "__main__":
    main()
