# brain_games/games/even.py
import prompt


def get_user_answer():
    return prompt.string('Your answer: ')


def is_even(number):
    return number % 2 == 0


def check_answer(number, user_answer):
    correct_answer = 'yes' if is_even(number) else 'no'
    if user_answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        return False


def play_even_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0
    while correct_answers < 3:
        number = random.randint(1, 100)
        print(f'Question: {number}')

        user_answer = get_user_answer()
        if check_answer(number, user_answer):
            correct_answers += 1
        else:
            print("Let's try again!")
            return

    print('Congratulations, you have won!')
