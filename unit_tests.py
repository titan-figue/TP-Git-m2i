
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

if __name__ == '__main__':
    unittest.main()