import unittest
from ex4 import isPassword_valid

class Testex4(unittest.TestCase):
    
    def test_valid_password(self):
        self.assertTrue(isPassword_valid('Shreya123#'))

    def test_invalid_password_less_than_minLength(self):
        self.assertFalse(isPassword_valid('Sh23#'))
    
    def test_invalid_password_more_than_maxLength(self):
        self.assertFalse(isPassword_valid('ssssAAAAAAAA1111111111@@@@@'))
    
    def test_invalid_password_missingCharacter(self):
        self.assertFalse(isPassword_valid('Sh23reya1'))
    
if __name__ == "__main__":
    unittest.main()