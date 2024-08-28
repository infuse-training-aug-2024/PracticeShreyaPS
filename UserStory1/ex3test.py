import unittest
from ex3 import skip_sports

class Testex1(unittest.TestCase):

    def test_valid_(self):
        self.assertEqual(skip_sports(2), {3: 'nnnn', 4: 'iiii'})

    

if __name__ == "__main__":
    unittest.main()