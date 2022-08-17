
import unittest
from main import *

class TestNbElement(unittest.TestCase):


    def setUp(self):
        self.name= "kraken"
    def test_monstre(self):
        result = randomMonster(self.name)
        self.assertAlmostEqual(len(result) ,4)

class GenerationDuMonstre(unittest.TestCase):
    def setUp(self):
        self.name = "toto"
    def test_function_generation_du_monstre(self):
        result = function_generation_du_monstre()
        print(result)
        test_name=result[0]
        self.assertRegex(test_name,r'[a-zA-Z0-9]')

class TestPersonnage(unittest.TestCase):
    def setUp(self):
        self.PV = 50
        self.Pseudo = 'toto'
        self.Force =  10
        self.Armure =  5
    def test_personnage(self):
        result = personnage (self.Pseudo, self.PV, self.Force, self.Armure)
        self.assertAlmostEqual(len(result), 4)

#a modifier
class TestTypeGestionDegats(unittest.TestCase):
   def setUp(self):
        self.foreceAtk = 50
        self.pvDefenseur = 150
        self.ArmureDefenseur =  10
   def function_gestion_degats(self):
        result = function_gestion_degats()
        print(result)
        self.assertRegex(result,r'[0-9]')

if __name__ == "__main__":
    unittest.main()