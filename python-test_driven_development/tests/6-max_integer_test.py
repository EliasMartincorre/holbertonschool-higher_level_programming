#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
   def test_maxinteger(self):
        self.assertEqual(max_integer([3, 4, 5]), 5)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer({}), None)
        self.assertEqual(max_integer([3, 4, -5]), 4)
        self.assertIsInstance(max_integer([3, 3, 4]), int)
        self.assertEqual(max_integer([85, 2, 4]), 85)

if __name__ == '__main__':
    unittest.main()
