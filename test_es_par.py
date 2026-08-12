import unittest

from math_utils import es_par # Aún no existe -> queremos ver fallar RED

class TestEsPar(unittest.TestCase):
    def test_4_es_par(self):
        self.assertTrue(es_par(4)) # 4 Debería de ser par
    
    def test_7_es_par(self):
        self.assertFalse(es_par(7))
    
    def test_0_es_par(self):
        self.assertTrue(es_par(0))
    
    def test_negativo_1_es_par(self):
        self.assertFalse(es_par(-7))
    
    def test_negativo_2_es_par(self):
        self.assertTrue(es_par(-6))

if __name__ == "__main__":
    unittest.main()