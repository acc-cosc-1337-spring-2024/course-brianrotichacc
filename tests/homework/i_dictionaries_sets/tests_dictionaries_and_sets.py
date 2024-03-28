import unittest
from src.homework.i_dictionaries_sets.dictionary import add_inventory
from src.homework.i_dictionaries_sets.dictionary import remove_inventory_widget,inventory


class Test_Config(unittest.TestCase):

    def test_add_inventory(self):
        inventory = {}
        add_inventory(inventory,'widget1',10)
        self.assertEqual(inventory,{'widget1': 10})
        add_inventory(inventory,'widget1',25)
        self.assertEqual(inventory,{'widget1': 35})
        add_inventory(inventory,'widget1',-10)
        self.assertEqual(inventory,{'widget1': 25})
    
    def test_remove_inventory_widget(self):
        remove_inventory_widget('widget1')
        self.assertEqual(len(inventory), 1)