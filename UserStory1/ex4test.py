
import unittest
from ex4 import PasswordValdation

class TestPasswordValidation(unittest.TestCase):

    def test_valid_passwords(self):
        pv = PasswordValdation()
        pv.isPassword_valid(['Password1@', 'Valid123#', 'GoodPass@1'])
        self.assertEqual(pv.valid_password_list, ['Password1@', 'Valid123#', 'GoodPass@1'])

    def test_invalid_passwords(self):
        pv = PasswordValdation()
        pv.isPassword_valid(['invalid', '12345', 'NoSpecialChar1', 'TOOSHORT1@'])
        self.assertEqual(pv.valid_password_list, [])

    def test_mixed_passwords(self):
        pv = PasswordValdation()
        pv.isPassword_valid(['Valid1#', 'invalid', 'Valid2@', 'short1'])
        self.assertEqual(pv.valid_password_list, ['Valid1#', 'Valid2@'])

    def test_empty_input(self):
        pv = PasswordValdation()
        pv.isPassword_valid([])
        self.assertEqual(pv.valid_password_list, [])

if __name__ == '__main__':
    unittest.main()
