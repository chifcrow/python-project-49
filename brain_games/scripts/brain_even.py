#!/usr/bin/env python3

from brain_games.cli.cli import welcome_user
from brain_games.games.even import play_even_game


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()

    if play_even_game():
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


if __name__ == '__main__':
    main()
