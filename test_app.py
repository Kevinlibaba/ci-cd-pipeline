import unittest
from app import add

class TestApp(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 2), 4)  # Corrected expected result

    def test_add_negative(self):
        self.assertEqual(add(-1, 4), 3)  # Corrected expected result

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)  # Already correct

    def test_add_mixed(self):
        self.assertEqual(add(-1, -1), -2)  # Already correct

    def test_add_large_numbers(self):
        self.assertEqual(add(1000, 2000), 3000)  # Already correct

"""Why Intentional Failures?
   Intentional failures are included to demonstrate that the testing system correctly identifies issues and highlights failures."""

if __name__ == "__main__":
    unittest.main()