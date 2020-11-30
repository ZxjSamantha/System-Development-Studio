import unittest
from BM1 import *

class TestBM1(unittest.TestCase):

    def test_finalState(self):
        self.assertEqual([1,0,1,0], update([0, 0, 0, 0]))
        self.assertNotEqual([1,0,1,1], update([0, 0, 0, 0]))
    
    def test_finalEnergy(self):
        self.assertEqual(0, energyFunc(update([0, 0, 0, 0])))
        self.assertNotEqual(1, energyFunc(update([0, 0, 0, 0])))

if __name__ =='__main__':
    unittest.main()

