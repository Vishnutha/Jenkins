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
        result = subtraction(data[0],data[1])
        self.assertEqual(result, 12)
    def test_addition(self):
        result = addition(1,3)
        self.assertEqual(result, 4)
    def test_subtraction_3(self):
        result = subtraction(1,3)
        self.assertEqual(result, 2)
    def test_mul_1(self):
        result = multiplication(2,3)
        self.assertEqual(result, 4)
    def test_addition_2(self):
        result = addition(1,3)
        self.assertEqual(result, 5)
        
   
        
        
     

if __name__ == '__main__':
    unittest.main()
