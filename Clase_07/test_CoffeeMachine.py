from Coffee_Machine import CoffeeMachine

import unittest

class CoffeeMachineTest(unittest.TestCase):

    def test_initial(self):
        machine = CoffeeMachine()
        self.assertEqual(machine.coins, 0)

    def test_insert_coin(self):
        machine = CoffeeMachine()
        machine.insert_coin()
        self.assertEqual(machine.coins, 1)

    def setUp(self):
        self.coffee = CoffeeMachine()

    def test_cafe_solo(self):
        self.assertEqual(self.coffee.cafetera(1), 'Haciendo cafe')
        self.assertEqual(self.coffee.water_amount(10), 'Con 10ml de agua')
        self.assertEqual(self.coffee.coffee_amount(5), 'Con 5gr de cafe')
        self.assertEqual(self.coffee.sugar_amount(0), 'Sin azucar')

    def test_cafe(self):
        self.assertEqual(self.coffee.cafetera(1), 'Haciendo cafe')
        self.assertEqual(self.coffee.water_amount(10), 'Con 10ml de agua')
        self.assertEqual(self.coffee.coffee_amount(7), 'Con 7gr de cafe')
        self.assertEqual(self.coffee.sugar_amount(3), 'Con 3gr de azucar')

    #Hacemos de cuenta que el producto en la cafetera es menor a la que necesita el vaso
    def test_cafe_agua_insuficiente(self):
        self.assertEqual(self.coffee.cafetera(1), 'Haciendo cafe')
        self.assertEqual(self.coffee.water_amount(9999), 'No hay agua suficiente')

    def test_cafe_cafe_insuficiente(self):
        self.assertEqual(self.coffee.cafetera(1), 'Haciendo cafe')
        self.assertEqual(self.coffee.water_amount(10), 'Con 10ml de agua')
        self.assertEqual(self.coffee.coffee_amount(9999), 'No hay cafe suficiente')

    def test_cafe_azucar_insuficiente(self):
        self.assertEqual(self.coffee.cafetera(1), 'Haciendo cafe')
        self.assertEqual(self.coffee.water_amount(10), 'Con 10ml de agua')
        self.assertEqual(self.coffee.coffee_amount(5), 'Con 5gr de cafe')
        self.assertEqual(self.coffee.sugar_amount(9999), 'No hay azucar suficiente')

if __name__ == "__main__":
    unittest.main()