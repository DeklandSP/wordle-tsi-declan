# Project name: Wordle
# Created by: Declan S P McCormack

# Project imports
import pathlib
from random import choice
from rich.console import Console

terminal = Console(width=60)
terminal.rule(":cherry_blossom: WORDLE :cherry_blossom:")


def start_game():
    WORD = get_random_word()
    print(WORD)
    guesses = ["_" * 5] * 6
    for attempt in range(6):
        print("Guess the word!")
        guesses[attempt] = get_users_guess()

        show_guess_results(guesses[attempt], WORD)
        if guesses[attempt] == WORD:
            terminal.print(":+1: Correct!")
            break
    end_game()


def get_random_word() -> str:
    WORDLIST_FILE_PATH = pathlib.Path('word_list.txt')
    WORDS = [words.upper() for words in WORDLIST_FILE_PATH.read_text(encoding='utf-8').strip().split('\n')
             if len(words) == 5]
    return choice(WORDS)


def get_users_guess() -> str:
    users_guess = input()
    return users_guess.upper()


def show_guess_results(users_answer, WORD):
    valid_letters = {letters for letters, valid in zip(users_answer, WORD) if letters == valid}
    incorrect_letters = set(users_answer) - set(WORD)
    letters_in_wrong_position = set(users_answer) & set(WORD) - valid_letters
    print('Valid Letters:', ', '.join(sorted(valid_letters)))
    print('incorrect letters:', ', '.join(sorted(incorrect_letters)))
    print('Wrong Position Letters:', ', '.join(sorted(letters_in_wrong_position)))
    refresh_terminal()


def end_game():
    print("Thank you for playing!")
    exit(0)


def refresh_terminal():
    terminal.clear()
    terminal.rule(f":cherry_blossom: WORDLE :cherry_blossom: \n")


if __name__ == '__main__':
    start_game()

