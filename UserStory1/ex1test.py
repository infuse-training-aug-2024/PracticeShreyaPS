import unittest
# import pytest
from ex1 import get_average
from ex1 import split_number

class SerialAverageTest(unittest.TestCase):
    
    def test_average(self):
        self.assertEqual(get_average(10.00,20.00), '15.00')

    def test_split_serial(self):
        self.assertEqual(split_number(),'888-15.00')
    

# ...

if __name__ == "__main__":
    unittest.main()