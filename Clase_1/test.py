import unittest
from suma import suma
class TestCalculator(unittest.TestCase):
    def testSuma(self):
        resultado = suma(2, 3)
        self.assertEqual(5,resultado)

if __name__ == "__main__":
    unittest.main()