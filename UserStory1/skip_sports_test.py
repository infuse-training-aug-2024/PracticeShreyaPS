import unittest
from ex3 import SkipSports

class SkipSportsTest(unittest.TestCase):
    sports_list = ['Football', 'Basketball', 'Tennis', 'Baseball', 'Hockey']


    def test_valid_input(self):
        skip_integer = 2
        expected_output = ['2:Tennis', '3:Baseball', '4:Hockey']
        actual_output=SkipSports().skip_sports(SkipSportsTest().sports_list,skip_integer)
        self.assertEqual(expected_output,actual_output)

    def test_negative_skip_integer(self):
        skip_integer = -2
        result=SkipSports().skip_sports(SkipSportsTest.sports_list,skip_integer)
        self.assertIsNone(result)
    
    def test_out_of_bound_skip_integer(self):
        skip_integer = 6
        result=SkipSports().skip_sports(SkipSportsTest.sports_list,skip_integer)
        self.assertIsNone(result)

    def test_left_bound_skip_integer(self):
        skip_integer = 0
        expected_output=['0:Football', '1:Basketball', '2:Tennis', '3:Baseball', '4:Hockey']
        actual_output=SkipSports().skip_sports(SkipSportsTest.sports_list,skip_integer)
        self.assertEqual(expected_output,actual_output)

    def test_right_bound_skip_integer(self):
        skip_integer = 5
        actual_output=SkipSports().skip_sports(SkipSportsTest.sports_list,skip_integer)
        self.assertIsNone(actual_output)
        
    def test_skip_integr_not_numerical(self):
        skip_integer = 'three'
        actual_output=SkipSports().skip_sports(SkipSportsTest.sports_list,skip_integer)
        self.assertIsNone(actual_output)

    

if __name__ == "__main__":
    unittest.main()

 