'''Test function for translate function'''
import unittest

from aegisbot.functions.translate import translate

class NamesTestCase(unittest.TestCase):
    def test_translation(self):
        translated=translate('id big')
        self.assertEqual('besar',translated)
unittest.main()
