import unittest
from ex2 import RangeFunctions

class TestRangeFunctions(unittest.TestCase):


    def test_element_at_valid_index(self):
        result = RangeFunctions().element_at(RangeFunctions.arr, 2)
        self.assertEqual(result, '1')

    def test_element_at_invalid_index(self):
        with self.assertRaises(IndexError):
            RangeFunctions().element_at(RangeFunctions.arr, 10)

    def test_inclusive_range_valid(self):
        result = RangeFunctions().inclusive_range(RangeFunctions.arr, 2, 4)
        self.assertEqual(result, ['1', '2', '3'])

    def test_inclusive_range_invalid(self):
        result = RangeFunctions().inclusive_range(RangeFunctions.arr, 2, 10)
        self.assertEqual(result, ['1', '2', '3', '4', '0', '-1'])

    def test_non_inclusive_range_valid(self):
        result = RangeFunctions().non_inclusive_range(RangeFunctions.arr, 2, 4)
        self.assertEqual(result, ['1', '2'])

    def test_non_inclusive_range_invalid(self):
        result = RangeFunctions().non_inclusive_range(RangeFunctions.arr, 2, 10)
        self.assertEqual(result, ['1', '2', '3', '4', '0', '-1'])

    def test_start_and_length_valid(self):
        result = RangeFunctions().start_and_length(RangeFunctions.arr, 2, 3)
        self.assertEqual(result, ['1', '2', '3'])

    def test_start_and_length_out_of_bounds(self):
        result = RangeFunctions().start_and_length(RangeFunctions.arr, 6, 5)
        self.assertEqual(result, ['0', '-1'])

if __name__ == '__main__':
    unittest.main()
