import builtins
import unittest
from unittest import mock
from unittest.mock import mock_open, patch
import pathlib
from app.wordle import *

class Wordle_unit_tests(unittest.TestCase):


    def test_get_random_word_from_file(self):
        filepath = pathlib.Path("word_list.txt")
        words = [word.upper() for word in filepath.read_text(encoding='utf-8').strip().split('\n')]
        self.assertTrue(get_random_word() in words)

    def test_stub_get_random_word(self):
        def get_random_word():
            return "alibi"

        with patch("builtins.open", mock_open(read_data="alibi")) as word:
            self.assertEqual("alibi", get_random_word())

    def test_end_game_print_win(self):
        self.assertEqual("string correct!", end_game(["alibi"], "alibi"))

    def test_end_game_print_lose(self):
        self.assertEqual("string incorrect!", end_game(["admin"], "alibi"))

    @mock.patch('builtins.input', side_effects=["ADMIN", "WOOZY", "WOOLY", "WELCH"])
    def test_mock_get_input(self, mock_input):
        first_call = mock_input
        second_call = mock_input
        third_call = mock_input
        fourth_call = mock_input

        self.assertTrue(first_call == "ADMIN" and second_call == "WOOZY"
                        and third_call == "WOOLY" and fourth_call == "WELCH")

if __name__ == '__main__':
    unittest.main()
