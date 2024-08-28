import unittest
# import pytest
from ex5 import GuessingGame

class Testex1(unittest.TestCase):

    def test_guess_match(self):
        game=GuessingGame(['s','h','i','r','t'],3)
        self.assertTrue(game.is_guess_match(['s','h','i','r','t']))

    def test_is_char_present(self):
        game=GuessingGame(['s','h','i','r','t'],3)
        self.assertTrue(game.is_char_present(['i']))

if __name__ == "__main__":
    unittest.main()