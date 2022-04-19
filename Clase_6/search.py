import unittest

# def search(lista, valor):
#     return valor in lista

def search(lista, valor):
    start = 0
    end = len(lista) - 1
    while end >= start:
        mid = (end + start) // 2
        if lista[mid] == valor:
            return True
        if end == start:
            break
        if lista[mid] > valor:
            end = mid - 1
        else:
            start = mid + 1
    return False



class TestSearch(unittest.TestCase):
    def test_simple(self):
        lista = [1]
        encontrado = search(lista, 1)
        self.assertTrue(encontrado)


    def test_simple_not_found(self):
        lista = [2]
        encontrado = search(lista, 1)
        self.assertFalse(encontrado)


    def test_complex(self):
        lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        encontrado = search(lista, 3)
        self.assertTrue(encontrado)

    def test_complex_not_found(self):
        lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        encontrado = search(lista, 10)
        self.assertFalse(encontrado)



if __name__ == '__main__':
    unittest.main()
    #revisar si un elemento está en el diccionario o no True o False