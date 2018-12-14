'''Test function for translate function'''
import unittest
import sys
sys.path.append('D:/1. College/DDP/TP4/functions/')
from translate import translate

class NamesTestCase(unittest.TestCase):
    def test_translation(self):
        translated=translate('id big')
        self.assertEqual('besar',translated)
unittest.main()
