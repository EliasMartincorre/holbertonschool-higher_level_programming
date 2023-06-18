#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
        unittests
    """

    def test_maxinteger(self):
        self.assertEqual(max_integer([3, 4, 5]), 5)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer({}), None)
        self.assertEqual(max_integer([3, 4, -5]), 4)
        self.assertIsInstance(max_integer([3, 3, 4]), int)
        self.assertEqual(max_integer([85, 2, 4]), 85)

    def test_error_maxinteger(self):
        self.assertRaises(TypeError, max_integer, ["F", 2, 3])
        self.assertRaises(KeyError, max_integer, {'r': 4, '4': 5})


if __name__ == '__main__':

    unittest.main()
