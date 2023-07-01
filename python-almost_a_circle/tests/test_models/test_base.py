#!/usr/bin/python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""
import unittest
from models.base import Base

class Base_TestCase(unittest.TestCase):
    """
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    def test_id(self):
        """ tests id"""
        a = Base()
        self.assertEqual(a.id, 1)
        b = Base()
        self.assertEqual(b.id, 2)
        c = Base(12)
        self.assertEqual(c.id, 12)
        d = Base()
        self.assertEqual(d.id, 3)
