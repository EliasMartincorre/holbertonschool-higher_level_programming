#!/usr/bin/python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""
import unittest
from models.rectangle import Rectangle

class Rectangle_TestCase(unittest.TestCase):
    """
    description
    """
    def test_id(self):
        """ test id heredado"""
        a = Rectangle(1, 2)
        self.assertEqual(a.id, 1)
        b = Rectangle(1, 1, 1, 1, 12)
        self.assertEqual(b.id, 12)
        c = Rectangle(12)
        self.assertEqual(c.id, 2)
        d = Rectangle()
        self.assertEqual(d.id, 3)