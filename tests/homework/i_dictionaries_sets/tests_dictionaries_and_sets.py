import unittest
from src.homework.i_dictionaries_sets.dictionary import add_inventory
from src.homework.i_dictionaries_sets.dictionary import remove_inventory_widget,inventory
from src.homework.i_dictionaries_sets.sets import get_students_who_took_prog1_and_prog2,get_students_who_took_prog1_or_prog2,get_students_who_took_prog1_not_prog2,get_students_who_took_prog2_not_prog1

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

    def test_get_students_who_took_prog1_and_prog2(self):
        prog1 = {'Student1', 'Student2', 'Student3'}
        prog2 = {'Student3', 'Student4', 'Student5'}
        self.assertEqual(get_students_who_took_prog1_and_prog2(prog1,prog2),{'Student3'})
    
    def test_get_students_who_took_prog1_or_prog2(self):
        prog1 = {'Student1', 'Student2', 'Student3'}
        prog2 = {'Student3', 'Student4', 'Student5'}
        self.assertEqual(get_students_who_took_prog1_or_prog2(prog1,prog2),{'Student1', 'Student2', 'Student3','Student4', 'Student5'})

    def test_get_students_who_took_prog1_not_prog2(self):
        prog1 = {'Student1', 'Student2', 'Student3'}
        prog2 = {'Student3', 'Student4', 'Student5'}
        self.assertEqual(get_students_who_took_prog1_not_prog2(prog1,prog2),{'Student1', 'Student2'})

    def test_get_students_who_took_prog2_not_prog1(self):
        prog1 = {'Student1', 'Student2', 'Student3'}
        prog2 = {'Student3', 'Student4', 'Student5'}
        self.assertEqual(get_students_who_took_prog2_not_prog1(prog1,prog2),{'Student4', 'Student5'})