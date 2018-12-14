'''Test function for calc function'''
import unittest
import sys
sys.path.append('D:/1. College/DDP/TP4/functions/')
from calc import calculate

class NamesTestCase(unittest.TestCase):
    def test_addition(self):
        res=int(calculate('2+4+3'))
        self.assertEqual(9,res)
    def test_substraction(self):
        res=int(calculate('2-4-3'))
        self.assertEqual(-5,res)
    def test_multiplication(self):
        res=int(calculate('2*4*3'))
        self.assertEqual(24,res)
    def test_divide(self):
        res=int(calculate('8/4'))
        self.assertEqual(2,res)
    def test_pow(self):
        res=int(calculate('10^4'))
        self.assertEqual(10000,res)
    def test_log(self):
        res=int(calculate('log(8,2)'))
        self.assertEqual(3,res)    
unittest.main()
