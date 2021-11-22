#!/usr/bin/python3
import unittest
from input import *
from math import *

class Test(unittest.TestCase):
    def test_add(self):
        for i in range(3):
            self.assertEqual(add(a[i], b[i]), add_expected[i])

    
    def test_sub(self):
        for i in range(3):
            self.assertEqual(subtract(a[i], b[i]), sub_expected[i])


    def test_div(self):
        for i in range(3):
            self.assertEqual(div(a[i], b[i]), div_expected[i])


    def test_mul(self):
        for i in range(3):
            self.assertEqual(mul(a[i], b[i]), mul_expected[i])

if __name__=="__main__":
    unittest.main()
