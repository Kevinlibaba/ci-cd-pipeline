import unittest
from app import add

class TestApp(unittest.TestCase):
    # Test cases that will pass
    def test_multiply_positive(self): 
        #Verifies multiplication of two positive numbers (e.g., 3 * 4).
        self.assertEqual(add(3, 4), 12)  # 3 * 4 = 12

    def test_multiply_zero(self): 
        #Tests multiplication of a number with zero (e.g., 5 * 0).
        self.assertEqual(add(5, 0), 0)  # 5 * 0 = 0

    def test_multiply_negative(self): 
        #Ensures correct behavior when multiplying a negative and a positive number (e.g., -2 * 3).
        self.assertEqual(add(-2, 3), -6)  # -2 * 3 = -6

    # Test cases that will fail intentionally
    def test_multiply_fail(self):
        #Purposefully provides an incorrect expected result for 2 * 2.
        self.assertEqual(add(2, 2), 5)  # Incorrect expected result

    def test_multiply_fail_negative(self):
        # Intentionally fails for -1 * 4 by providing an incorrect expected value.
        self.assertEqual(add(-1, 4), 0)  # Incorrect expected result

"""Why Intentional Failures?
   Intentional failures are included to demonstrate that the testing system correctly identifies issues and highlights failures."""

if __name__ == "__main__":
    unittest.main()