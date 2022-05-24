import unittest


class CoffeeMachine:

    def __init__(self):
        self.coins = 0
        self.water = 6500
        self.coffee = 500
        self.sugar = 250

    def insert_coin(self):
        self.coins += 1

    def insert_coffee(self, coffee):
        self.coffee += coffee

    def insert_sugar(self, sugar):
        self.sugar += sugar
        
    def cafetera(self):
        if self.coins > 0:
            if self.water == 0:
                return 'No hay agua'
            if self.coffee == 0:
                return 'No hay cafe'
            if self.sugar == 0:
                return 'No hay azucar'
            else:
                self.coins -= 1
                self.coffee -= 7
                self.water -= 200
                self.sugar -= 5
                return 'Haciendo cafe'   

    def count_coffee(self):
        count_coffee_because_coffee = self.coffee // 7
        count_coffee_because_sugar = self.sugar // 5
        return min(count_coffee_because_coffee, count_coffee_because_sugar)

if __name__ == '__main__':
    unittest.main()