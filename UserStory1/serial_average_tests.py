import unittest
from ex1 import SerialAverage

class TestSerialAverage(unittest.TestCase):

    def test_split_number_valid_input(self):
        result = SerialAverage().split_number('333-00.10-00.20')
        self.assertEqual(result, '333-00.15')

    def test_split_number_invalid_format(self):
        result = SerialAverage().split_number('333-0000-10.00')
        self.assertIsNone(result)

    def test_split_number_left_boundary_input(self):
        result = SerialAverage().split_number('333-00.00-00.01')
        self.assertEqual(result, '333-00.01')

    def test_split_number_right_boundary_input(self):
        result = SerialAverage().split_number('333-99.98-99.99')
        self.assertEqual(result, '333-99.98')

    def test_split_number_non_numeric(self):
        result = SerialAverage().split_number('333-aa.bb-cc.dd')
        self.assertIsNone(result)

    def test_split_number_empty_input(self):
        result = SerialAverage().split_number('')
        self.assertIsNone(result)

    def test_check_for_single_digit(self):
        result = SerialAverage().check_for_single_digit('5.34')
        self.assertEqual(result, '05.34')

        result = SerialAverage().check_for_single_digit('15.34')
        self.assertEqual(result, '15.34')

    def test_get_average_valid_numbers(self):
        result = SerialAverage().get_average(10.00, 20.00)
        self.assertEqual(result, '15.00')

    def test_get_average_invalid_number(self):
        result = SerialAverage().get_average('abc', 10.00)
        self.assertIsNone(result)

    def test_split_number_correct_average(self):
        result = SerialAverage().split_number('111-10.00-20.00')
        self.assertEqual(result, '111-15.00')

    

if __name__ == '__main__':
    unittest.main()













# class SerialAverageTest(unittest.TestCase):
    
#     def test_average(self):
#         number1=int(input("enter 1st number:"))
#         number2=int(input("enter 2nd number:"))
#         self.assertEqual(get_average(number1,number2), '15.00')

#     def test_split_serial(self):
#         self.assertEqual(split_number(),'888-15.00')
    



# if __name__ == "__main__":
#     unittest.main()