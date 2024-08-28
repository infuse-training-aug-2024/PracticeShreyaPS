import unittest
from ex2 import range_functions

class Testex2(unittest.TestCase):
    def test_is_instance(self):
        obj=range_functions(3,4,6)
        self.assertIsInstance(obj,range_functions)
    
    def test_correct_index(self):
        obj=range_functions(3,4,5)
        arr=['9','5','1','2','3','4','0','-1']
        self.assertEqual(obj.element_at(arr),'2')

    def test_correct_last_element(self):
        obj=range_functions(3,4,5)
        arr=['9','5','1','2','3','4','0','-1']
        self.assertNotIn(obj.non_inclusive_range(arr),'0')
        self.assertIn(obj.inclusive_range(arr),'0')

    
if __name__ == "__main__":
    unittest.main()