import unittest
from services.calc import addition

def addition(a, b):
    return a + b

class TestAddition(unittest.TestCase):

    def test_addition_positive_numbers(self):
        self.assertEqual(addition(3, 5), 8)

    def test_addition_negative_numbers(self):
        self.assertEqual(addition(-3, -5), -8)

    def test_addition_mixed_numbers(self):
        self.assertEqual(addition(-3, 5), 2)

if __name__ == '__main__':
    unittest.main()
