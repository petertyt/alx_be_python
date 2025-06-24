import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test addition of positive, negative, and zero values."""
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtraction(self):
        """Test subtraction for various combinations."""
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiply(self):
        """Test multiplication with positives, negatives, and zero."""
        self.assertEqual(self.calc.multiply(2, 4), 8)

    def test_divide(self):
        """Test division, including division by zero."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(3, 0), None)

    def test_division_precision(self):
        """Test float precision in division."""
        self.assertAlmostEqual(self.calc.divide(1, 3), 1/3, places=7)

if __name__ == "__main__":
    unittest.main()