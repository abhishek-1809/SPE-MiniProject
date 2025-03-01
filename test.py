import unittest
import math
from io import StringIO
import sys

from calculator import main 

class TestScientificCalculator(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(math.factorial(0), 1)
        self.assertEqual(math.factorial(4), 24)
            
    def test_square_root(self):
        self.assertEqual(math.sqrt(0), 0)
        self.assertEqual(math.sqrt(4), 2)
    
    def test_natural_log(self):
        self.assertAlmostEqual(math.log(1), 0, places=4)
        self.assertAlmostEqual(math.log(math.e), 1, places=4)
    
    def test_power_function(self):
        self.assertEqual(math.pow(3, 2), 9)
        self.assertEqual(math.pow(8, 0), 1)
    
    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            math.sqrt(-1)
        with self.assertRaises(ValueError):
            math.log(0)
        with self.assertRaises(ValueError):
            math.log(-5)
    
if __name__ == "__main__":
    unittest.main()
