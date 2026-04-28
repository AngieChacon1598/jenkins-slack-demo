"""
Tests unitarios con errores simulados
Este archivo se usa para demostrar cómo se comporta el pipeline cuando hay fallos
"""
import unittest
from app import sumar, restar, multiplicar, dividir

class TestCalculadora(unittest.TestCase):
    
    def test_sumar(self):
        self.assertEqual(sumar(5, 3), 8)
        self.assertEqual(sumar(-1, 1), 0)
    
    def test_restar(self):
        # Este test fallará intencionalmente
        self.assertEqual(restar(10, 4), 7)  # Debería ser 6
    
    def test_multiplicar(self):
        # Este test también fallará
        self.assertEqual(multiplicar(6, 7), 40)  # Debería ser 42
    
    def test_dividir(self):
        self.assertEqual(dividir(20, 4), 5)
        self.assertEqual(dividir(10, 2), 5)
    
    def test_dividir_por_cero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)

if __name__ == '__main__':
    unittest.main()
