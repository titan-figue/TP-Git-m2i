#!/usr/bin/python3
import unittest
from main import *
class TestPersonnage(unittest.TestCase):
    def setUp(self): 
        self.PV = 50
    def test_personnage(self):
 #       result = self.assertTrue ( (self.PV).isnumber(), msg=None)
        result = self.assertTrue (str(self.PV).startswith('50'))
    
if __name__ == "__main__":
    unittest.main()