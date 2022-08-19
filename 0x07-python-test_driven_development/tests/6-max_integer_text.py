""" Unittest for max_integer([...]) """

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        #test when a proper list is given
        self.assertEqual(max_integer([1,2,3,4]), 4)
        self.assertEqual(max_integer([1,3,4,2]), 4)
        self.assertEqual(max_integer([]), None)
    
    def test_values(self):
        #test the values to to make sure value errors are raised
        self.assertRaises(TypeError, max_integer, ["hello", 1, 3, 4])
