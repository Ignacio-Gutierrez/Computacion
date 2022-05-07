import unittest

def funcion():
    return 0

class test(unittest.TestCase):
    def test_esto_siempre_esta_bien(self):
        self.assertTrue(funcion)

if __name__ == '__main__':
    unittest.main()