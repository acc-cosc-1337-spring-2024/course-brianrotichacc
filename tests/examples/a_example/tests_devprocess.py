import unittest

from src.examples.a_example.devprocess import add_numbers, subtract_numbers

class Test_Config(unittest.TestCase):

    def test_add_numbers_2(self):
        self.assertEqual(2, add_numbers(1, 1))

    def test_subtract_number_1(self):
        self.assertEquals(5, subtract_numbers(10,5))

