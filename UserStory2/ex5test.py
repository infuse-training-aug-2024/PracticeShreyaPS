import unittest
import csv
import os
from ex5 import GuessingGame, read_secret_word_from_file

class TestGuessingGame(unittest.TestCase):

    def setUp(self):
        self.secret_word = ['s', 'h', 'i', 'r', 't']
        self.game = GuessingGame(self.secret_word, 3)
        self.test_username = "testuser"
        self.test_score_file = 'UserStory2/scores.csv'

        with open(self.test_score_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'score'])

    def tearDown(self):
        if os.path.isfile(self.test_score_file):
            os.remove(self.test_score_file)

    def test_is_guess_match(self):
        guess = ['s', 'h', 'i', 'r', 't']
        self.assertTrue(self.game.is_guess_match(guess))

        guess = ['s', 'h', 'o', 'e', 's']
        self.assertFalse(self.game.is_guess_match(guess))

    def test_is_char_present(self):
        self.assertTrue(self.game.is_char_present(['s']))
        self.assertFalse(self.game.is_char_present(['z']))

    def test_update_csv_new_user(self):
        self.game.update_csv(self.test_username)
        with open(self.test_score_file, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            self.assertEqual(rows[1], [self.test_username, '3'])

    def test_update_csv_existing_user(self):
        self.game.update_csv(self.test_username)
        self.game.lives = 2
        self.game.update_csv(self.test_username)
        with open(self.test_score_file, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            self.assertEqual(rows[1], [self.test_username, '2'])

    def test_view_score_existing_user(self):
        self.game.update_csv(self.test_username)
        self.game.lives = 1
        self.game.update_csv(self.test_username)

        with open(self.test_score_file, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            self.assertEqual(rows[1], [self.test_username, '1'])

    def test_view_score_no_scores(self):
        output = self.game.view_score('nonexistent_user')
        self.assertIsNone(output)  

    def test_read_secret_word_from_file(self):
        secret_word = read_secret_word_from_file('UserStory2/secret_word.txt')
        self.assertIsInstance(secret_word, list)
        self.assertGreater(len(secret_word), 0)

if __name__ == '__main__':
    unittest.main()
