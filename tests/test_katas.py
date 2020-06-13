import unittest
import katas
import math

class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(7,3), 7+3)

    def test_multiply(self):
        self.assertEqual(katas.multiply(7,3), 7*3)

    def test_power(self):
        self.assertEqual(katas.power(5,5), math.pow(5,5))

    def test_factorial(self):
        self.assertEqual(katas.factorial(8), math.factorial(8))

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(9),21)


if __name__ == '__main__':
    unittest.main()
