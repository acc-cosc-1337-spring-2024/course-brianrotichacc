import unittest
'''
the file in /tests/homework/i_dictionaries_and_sets/tests_dictionaries_sets
has tests dictionaries sets
'''
from tests.homework.j_classes import tests_classes

suite = unittest.TestLoader().loadTestsFromModule(tests_classes)
unittest.TextTestRunner(verbosity=2).run(suite)
