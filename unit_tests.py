import unittest
from main import *

class TestNbElement(unittest.TestCase):


    def setUp(self):
        self.name= "kraken"
    def test_monstre(self):
        result = randomMonster(self.name)
        self.assertAlmostEqual(len(result) ,4)

if __name__ == '__main__':
    unittest.main()