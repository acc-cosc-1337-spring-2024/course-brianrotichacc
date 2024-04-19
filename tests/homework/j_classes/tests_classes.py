import unittest
from src.homework.j_classes.class_a import die

class Test_Config(unittest.TestCase):

    def test_die_roll(self):
        die1 = die()
        die1.roll()
        rolled_value = die1.get_rolled_value()
        self.assertTrue(1 <= rolled_value <=6, "Roll value out of range")
        die1.roll()
        rolled_value1 = die1.get_rolled_value()
        self.assertTrue(1 <= rolled_value1 <=6, "Roll value out of range")
        die1.roll()
        rolled_value2 = die1.get_rolled_value()
        self.assertTrue(1 <= rolled_value2 <=6, "Roll value out of range")
