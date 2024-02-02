import unittest

from src.examples.c_decisions.decisions import get_and_result, get_not_result, get_or_result, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())
    
    def test_and_truth_table(self):
        self.assertEqual(get_and_result(True, True), True)
        self.assertEqual(get_and_result(True, False), False)
        self.assertEqual(get_and_result(False, True), False)
        self.assertEqual(get_and_result(False, False), False)

    def test_or_truth_table(self):
        self.assertEqual(get_or_result(True, True), True)
        self.assertEqual(get_or_result(True, False), True)
        self.assertEqual(get_or_result(False, True), True)
        self.assertEqual(get_or_result(False, False), False)

    def test_not_truth_table(self):
        self.assertEqual(get_not_result(True), False)
        self.assertEqual(get_not_result(False), True)
