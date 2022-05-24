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
        
    def test_cafe_solo(self):
        machine = CoffeeMachine()
        machine.insert_coin()
        self.assertEqual(machine.cafetera(), 'Haciendo cafe')
        self.assertEqual(machine.water, 6500-200)
        self.assertEqual(machine.coffee, 500-7)
        self.assertEqual(machine.sugar, 250-5)

    def test_insert_coffee(self):
        machine = CoffeeMachine()
        machine.insert_coffee(1000)
        self.assertEqual(machine.coffee, 500+1000)

    def test_insert_coffee_second_time(self):
        machine = CoffeeMachine()
        machine.insert_coffee(1000)
        machine.insert_coffee(1000)
        self.assertEqual(machine.coffee, 2500)

    def test_insert_sugar(self):
        machine = CoffeeMachine()
        machine.insert_sugar(1000)
        self.assertEqual(machine.sugar, 1250)

    def test_insert_coffee_second_time(self):
        machine = CoffeeMachine()
        machine.insert_sugar(1000)
        machine.insert_sugar(1000)
        self.assertEqual(machine.sugar, 2250)

    def test_get_coffee_ok(self):
        machine = CoffeeMachine()
        machine.insert_coin()
        machine.insert_coin()
        machine.insert_coffee(1000)
        machine.insert_sugar(1000)
        coffee_result = machine.cafetera()
        self.assertTrue(coffee_result)
        self.assertEqual(machine.coffee, 1500-7)
        self.assertEqual(machine.sugar, 1250-5)
        self.assertEqual(machine.coins, 1)

    def test_get_coffee_error_no_coffee(self):
        machine = CoffeeMachine()
        machine.insert_coin()
        machine.insert_coin()
        machine.insert_sugar(-250)
        coffee_result = machine.cafetera()
        self.assertEqual(machine.cafetera(), 'No hay azucar')
        self.assertEqual(machine.coffee, 500)
        self.assertEqual(machine.sugar, 0)
        self.assertEqual(machine.coins, 2)

    def test_get_coffee_error_no_sugar(self):
        machine = CoffeeMachine()
        machine.insert_coin()
        machine.insert_coin()
        machine.insert_sugar(-250)
        machine.insert_coffee(1000)
        coffee_result = machine.cafetera()
        self.assertEqual(coffee_result, 'No hay azucar')
        self.assertEqual(machine.sugar, 0)
        self.assertEqual(machine.coffee, 1500)
        self.assertEqual(machine.coins, 2)

    def test_get_coffee_error_no_coin(self):
        machine = CoffeeMachine()
        machine.insert_coffee(1000)
        machine.insert_sugar(1000)
        coffee_result = machine.cafetera()
        self.assertFalse(coffee_result)
        self.assertEqual(machine.sugar, 1250)
        self.assertEqual(machine.coffee, 1500)
        self.assertEqual(machine.coins, 0)

if __name__ == "__main__":
    unittest.main()