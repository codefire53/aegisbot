'''Test function for define function'''
import unittest

from aegisbot.functions.oxford import define

class NamesTestCase(unittest.TestCase):
    def test_definition(self):
        definitions=define('violation')
        self.assertEqual('List of definitions of "violation" word/phrase:\n1. (noun)The action of violating someone or something.\n',definitions)
unittest.main()
