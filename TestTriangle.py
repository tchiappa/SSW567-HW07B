# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):

    # --- Equilateral ---

    def testEquilateral_min(self):          # T01
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', 'T01: 1,1,1 should be Equilateral')

    def testEquilateral_mid(self):          # T02
        self.assertEqual(classifyTriangle(10, 10, 10), 'Equilateral', 'T02: 10,10,10 should be Equilateral')

    def testEquilateral_max(self):          # T03
        self.assertEqual(classifyTriangle(200, 200, 200), 'Equilateral', 'T03: 200,200,200 should be Equilateral')

    # --- Right ---

    def testRight_3_4_5(self):              # T04
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', 'T04: 3,4,5 should be Right')

    def testRight_5_3_4(self):              # T05
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', 'T05: 5,3,4 should be Right')

    def testRight_5_4_3(self):              # T06
        self.assertEqual(classifyTriangle(5, 4, 3), 'Right', 'T06: 5,4,3 should be Right')

    # --- Isosceles ---

    def testIsosceles_aEqualsB(self):       # T07
        self.assertEqual(classifyTriangle(3, 3, 2), 'Isosceles', 'T07: 3,3,2 should be Isosceles')

    def testIsosceles_aEqualsC(self):       # T08
        self.assertEqual(classifyTriangle(3, 2, 3), 'Isosceles', 'T08: 3,2,3 should be Isosceles')

    def testIsosceles_bEqualsC(self):       # T09
        self.assertEqual(classifyTriangle(2, 3, 3), 'Isosceles', 'T09: 2,3,3 should be Isosceles')

    # --- Scalene ---

    def testScalene(self):                  # T10
        self.assertEqual(classifyTriangle(3, 4, 6), 'Scalene', 'T10: 3,4,6 should be Scalene')

    # --- NotATriangle ---

    def testNotATriangle_degenerate(self):  # T11
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle', 'T11: 1,2,3 is degenerate (sum equals third side)')

    def testNotATriangle_clear(self):       # T12
        self.assertEqual(classifyTriangle(3, 3, 9), 'NotATriangle', 'T12: 3,3,9 is not a triangle')

    # --- InvalidInput: out of range ---

    def testInvalid_aExceedsMax(self):      # T13
        self.assertEqual(classifyTriangle(201, 1, 1), 'InvalidInput', 'T13: a=201 exceeds upper bound')

    def testInvalid_bExceedsMax(self):      # T14
        self.assertEqual(classifyTriangle(1, 201, 1), 'InvalidInput', 'T14: b=201 exceeds upper bound')

    def testInvalid_cExceedsMax(self):      # T15
        self.assertEqual(classifyTriangle(1, 1, 201), 'InvalidInput', 'T15: c=201 exceeds upper bound')

    def testInvalid_aNegative(self):        # T16
        self.assertEqual(classifyTriangle(-1, 1, 1), 'InvalidInput', 'T16: a=-1 is below valid range')

    # --- Boundary: zero (valid per spec, degenerate triangle) ---

    def testZero_a(self):                   # T17
        self.assertEqual(classifyTriangle(0, 1, 1), 'NotATriangle', 'T17: 0 is valid per spec; 0+1=1 is degenerate')

    # --- Boundary: upper valid boundary ---

    def testNotATriangle_upperBoundary(self):  # T18
        self.assertEqual(classifyTriangle(200, 1, 1), 'NotATriangle', 'T18: 200 is valid input; 1+1=2 < 200 not a triangle')

    # --- InvalidInput: wrong type ---

    def testInvalid_float(self):            # T19
        self.assertEqual(classifyTriangle(1.5, 2, 3), 'InvalidInput', 'T19: float input should be InvalidInput')

    def testInvalid_string(self):           # T20
        self.assertEqual(classifyTriangle("three", 1, 1), 'InvalidInput', 'T20: string input should be InvalidInput')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
