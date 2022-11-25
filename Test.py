#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from Prog1 import *

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        data = [20, 5]
        result = division(data[0],data[1])
        self.assertEqual(result, 4)
        
     

if __name__ == '__main__':
    unittest.main()
