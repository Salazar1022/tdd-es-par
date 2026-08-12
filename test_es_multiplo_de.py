import unittest

from math_utils import es_multiplo_de

class TestEsMultiplo(unittest.TestCase):
    
    def test_25_multiplo_de_5(self):
        self.assertTrue(es_multiplo_de(25, 5))

    def test_22_multiplo_de_3(self):
        self.assertFalse(es_multiplo_de(22, 3))

    def test_negativo_1_multiplo_de(self):
        self.assertTrue(es_multiplo_de(-100, 10))

    def test_negativo_2_multiplo_de(self):
        self.assertFalse(es_multiplo_de(-50, 7))

    def test_cero_1_multiplo_de(self):
        self.assertTrue(es_multiplo_de(0, 10))

    def test_cero_2_multiplo_de(self):
        self.assertFalse(es_multiplo_de(20, 0))
