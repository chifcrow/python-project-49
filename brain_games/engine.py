from prompt_toolkit import prompt


def run_game(game):
    print("Welcome to the Brain Games!")
    name = prompt('May I have your name? ')
    print(f"Hello, {name}!")

    rounds = 3

    for _ in range(rounds):
        question, correct_answer = game()
        print(f"Question: {question}")
        user_answer = prompt("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
