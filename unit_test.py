#!/usr/bin/python3
import unittest
from main import *
class TestPersonnage(unittest.TestCase):
    def setUp(self): 
        self.PV = 50
        self.Pseudo = 'toto'
        self.Force =  10
        self.Armure =  5
    def test_personnage(self):
        result = personnage (self.Pseudo, self.PV, self.Force, self.Armure)
        self.assertAlmostEqual(len(result), 4)
    
if __name__ == "__main__":
    unittest.main()