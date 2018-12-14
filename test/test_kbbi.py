'''Test Function for search function on kbbi module'''
import unittest

from aegisbot.functions.kbbi import search

class NamesTestCase(unittest.TestCase):
    def test_translate(self):
        word=search('Hiperbola')
        self.assertEqual('(n Mat) dua lengkungan terpisah yang merupakan perpotongan permukaan kerucut lingkar dengan bidang datar\n(n Mat) himpunan titik-titik yang selisih jaraknya terhadap dua titik tetap adalah konstan',word)
unittest.main()
