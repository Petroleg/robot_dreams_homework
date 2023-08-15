from HomeWork06.task1 import exponentiation
from HomeWork06.task2 import not_built_in_sum

from HomeWork06.task3 import maximum
import unittest


class TestExponentiation(unittest.TestCase):
    def test_exponentiation_positive(self):
        self.assertEqual(exponentiation(2, 3), 8)
        self.assertEqual(exponentiation(5, 2), 25)
        self.assertEqual(exponentiation(10, 0), 1)

    def test_exponentiation_negative(self):
        self.assertEqual(exponentiation(-2, 4), 16)
        self.assertEqual(exponentiation(-3, 3), -27)


class TestNotBuiltInSum(unittest.TestCase):
    def test_not_built_in_sum(self):
        self.assertEqual(not_built_in_sum(3, 51, 2, 11, 7), 74)
        self.assertEqual(not_built_in_sum(10, 20, 30, 40, 50), 150)


class TestMaximum(unittest.TestCase):
    def test_maximum_function(self):
        self.assertEqual(maximum([3, 15, 8, 23, 5]), 23)
        self.assertEqual(maximum([10, 20, 30, 40, 99]), 99)


if __name__ == '__main__':
    unittest.main()
