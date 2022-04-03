import unittest

def funcion_ok(a, b):
    return a + b


class PrimerTests(unittest.TestCase):
    def test_primera_funcion_ok(self):
        resultado = funcion_ok(5, 6)
        self.assertEqual(resultado, 11)



if __name__ == "__main__":
    unittest.main()