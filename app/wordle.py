# Project name: Wordle
# Created by: Declan S P McCormack

# Project imports
import pathlib
from random import choice
from rich.console import Console

terminal = Console(width=60)
terminal.rule(":cherry_blossom: WORDLE :cherry_blossom:")

def main():
    start_game()


def start_game():
    word = get_random_word()
    print(word)
    guesses = ["_" * 5] * 6
    for attempt in range(6):
        refresh_terminal(heading=f"Guess {attempt + 1}")
        show_guess_results(guesses, word)

        guesses[attempt] = get_input()
        if guesses[attempt] == word:
            break
    end_game(guesses, word)


def get_input() -> str:
    return input(f"\n Guess :").upper()

def get_random_word() -> str:
    WORDLIST_FILE_PATH = pathlib.Path('word_list.txt')
    WORDS = [words.upper() for words in WORDLIST_FILE_PATH.read_text(encoding='utf-8').strip().split('\n')
             if len(words) == 5]
    return choice(WORDS)


def show_guess_results(users_answer, word):
    for guess in users_answer:
        style_format = []
        for letter, valid in zip(guess, word):
            if letter == valid:
                format = "bold black on green"
            elif letter in word:
                format = "bold black on yellow"
            else:
                format = "bold black on red"
            style_format.append(f"[{format}] {letter}")
        terminal.print("".join(style_format), justify="center")


def end_game(guesses, word):
    refresh_terminal(heading="Game Finish")
    show_guess_results(guesses, word)

    if word in guesses:
        terminal.print(f"\n [bold black on green] Congrats, {word} was the correct one [/]")
        return "string correct!"
    else:
        terminal.print(f"\n [bold black on red] Bad luck, the correct word was {word} [/]")
        return "string incorrect!"


def refresh_terminal(heading):
    terminal.clear()
    terminal.rule(f":cherry_blossom: {heading} :cherry_blossom: \n")


if __name__ == '__main__':
    main()

