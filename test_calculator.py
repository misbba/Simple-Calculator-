"""
test_calculator.py - Unit tests for Smart Calculator mathematical functions.
"""

import unittest
from calculator import (
    add, subtract, multiply, divide, modulus,
    power, floor_divide, square_root, percentage, format_result
)

class TestCalculator(unittest.TestCase):
    
    def test_addition(self):
        self.assertEqual(add(10, 20), 30)
        self.assertEqual(add(-5, 15), 10)
        self.assertEqual(add(3.5, 2.5), 6.0)

    def test_subtraction(self):
        self.assertEqual(subtract(20, 5), 15)
        self.assertEqual(subtract(5, 20), -15)

    def test_multiplication(self):
        self.assertEqual(multiply(5, 4), 20)
        self.assertEqual(multiply(-3, 7), -21)

    def test_division(self):
        self.assertEqual(divide(20, 5), 4)
        self.assertAlmostEqual(divide(10, 3), 3.3333333, places=6)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError) as ctx:
            divide(10, 0)
        self.assertIn("Cannot divide by zero", str(ctx.exception))

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)

    def test_modulus_by_zero(self):
        with self.assertRaises(ValueError) as ctx:
            modulus(10, 0)
        self.assertIn("zero", str(ctx.exception))

    def test_power(self):
        self.assertEqual(power(2, 5), 32)
        self.assertEqual(power(9, 0.5), 3)

    def test_floor_division(self):
        self.assertEqual(floor_divide(20, 3), 6)

    def test_floor_division_by_zero(self):
        with self.assertRaises(ValueError) as ctx:
            floor_divide(10, 0)
        self.assertIn("zero", str(ctx.exception))

    def test_square_root(self):
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(0), 0)

    def test_square_root_negative(self):
        with self.assertRaises(ValueError) as ctx:
            square_root(-25)
        self.assertIn("negative", str(ctx.exception))

    def test_percentage(self):
        self.assertEqual(percentage(10, 500), 50)
        self.assertEqual(percentage(25, 200), 50)

    def test_format_result(self):
        self.assertEqual(format_result(30.0), 30)
        self.assertEqual(format_result(3.3333333), "3.333333")
        self.assertEqual(format_result(15), 15)

if __name__ == '__main__':
    unittest.main()
