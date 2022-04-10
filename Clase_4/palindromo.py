import unittest

def es_palindromo(palabra):
    
    palabra = palabra.lower()

    return palabra == palabra[::-1]
    
class Test_Palindromo(unittest.TestCase):

    def test_1(self):
        palindromo = es_palindromo("oso")
        self.assertEqual(palindromo, True)

    def test_2(self):
        palindromo = es_palindromo("neuquen")
        self.assertEqual(palindromo, True)

    def test_3(self):
        palindromo = es_palindromo("palabra")
        self.assertEqual(palindromo, False)

    def test_4(self):
        palindromo = es_palindromo("queso")
        self.assertEqual(palindromo, False)

    def test_4(self):
        palindromo = es_palindromo("papa")
        self.assertEqual(palindromo, False)

    def test_5(self):
        palindromo = es_palindromo('nEN')
        self.assertEqual(palindromo, True)

if __name__ == '__main__':
    unittest.main()