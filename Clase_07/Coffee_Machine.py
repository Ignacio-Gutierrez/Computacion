import unittest


class CoffeeMachine:

    def __init__(self):
        self.makingCoffe = False
        self.coins = 0
        self.water = 2500
        self.coffee = 500
        self.sugar = 250

    def insert_coin(self):
        self.coins += 1

    def cafetera(self, coins):
        self.coin = coins
        if self.coin > 0:
            if self.water == 0:
                return 'No hay agua'
            if self.coffee == 0:
                return 'No hay cafe'
            if self.sugar == 0:
                return 'No hay azucar'
            else:
                self.makingCoffee = True
                self.coin -= 1
                return 'Haciendo cafe'        

    def water_amount(self, water_ml):
        if self.makingCoffee == True:
            if water_ml > self.water:
                self.makingCoffee = False
                return 'No hay agua suficiente'
            else:
                self.water -= water_ml
                return 'Con '+ str(water_ml)+'ml de agua' 

    def coffee_amount(self, coffee_gr):
        if self.makingCoffee == True:
            if coffee_gr > self.coffee:
                self.makingCoffee = False
                return 'No hay cafe suficiente'
            else:
                self.coffee -= coffee_gr
                return 'Con ' + str(coffee_gr) + 'gr de cafe'

    def sugar_amount(self, sugar_gr):
        if self.makingCoffee == True:
            if sugar_gr > self.sugar:
                self.makingCoffee = False
                return 'No hay azucar suficiente'
            if sugar_gr == 0:
                return 'Sin azucar'
            else:
                self.sugar -= sugar_gr
                return 'Con ' + str(sugar_gr) + 'gr de azucar'  


class CoffeeMachineTest(unittest.TestCase):
    def test_initial(self):
        machine = CoffeeMachine()
        self.assertEqual(machine.coins, 0)

    def test_insert_coin(self):
        machine = CoffeeMachine()
        machine.insert_coin()
        self.assertEqual(machine.coins, 1)


if __name__ == '__main__':
    unittest.main()