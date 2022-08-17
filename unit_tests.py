#!/usr/bin/python3
import unittest
from main import *
class GenerationDuMonstre(unittest.TestCase):
    def setUp(self):
        self.name = "toto"
    def test_function_generation_du_monstre(self):
        result= function_generation_du_monstre(self.name)
        test_name=result[0]
        self.assertRegex(test_name,r'[a-zA-Z0-9]')
if __name__ == '__main__':
    unittest.main()