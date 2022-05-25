from collections import Counter

class MasterCoffeeMachine:

    def __init__(self):
        self.resources = {
            'coin': 0,
            'sugar': 250,
            'water': 6500,
            'coffee': 500,
            'milk': 2000,
            'chocolate': 20,
            'tea': 250,
        }
        self.recipies = {
            'coffee_alone': {
                'coffee': 7,
                'water': 200,
            },
            'coffee_double': {
                'coffee': 14,
                'water': 200,
            },
            'coffee_milk': {
                'coffee': 7,
                'water': 150,
                'milk': 50,
            },
            'coffee_milk_double': {
                'coffee': 14,
                'water': 150,
                'milk': 50,
            },
            'capuccino': {
                'coffee': 14,
                'chocolate': 1,
                'milk': 200
            },
            'tea_simple': {
                'tea': 20,
                'water': 200,
            },
        }


    def add_resource(self, type, amount):
        self.resources[type] += amount

    def chose_drink(self, election):
        self.election = election

    def CafeteraPlus(self):

        if self.resources['coin'] == 0:
            return 'Inserte una moneda'
        if self.resources['coin'] > 0:
            if self.resources['water'] == 0:
                return 'No hay agua'
            if self.resources['coffee'] == 0:
                return 'No hay café'
            if self.resources['sugar'] == 0:
                return 'No hay azucar'
            if self.resources['milk'] == 0:
                return 'No hay leche'      
            if self.resources['chocolate'] == 0:
                return 'No hay chocolate'
            if self.resources['tea'] == 0:
                return 'No hay té'     
            else:
                self.resources['coin'] -= 1
                self.resources['sugar'] -= 5

                if self.election == 1:
                    self.resources = Counter(self.resources) - Counter(self.recipies['coffee_alone'])
                    return 'Haciendo Café Simple'
                if self.election == 2:
                    self.resources = Counter(self.resources) - Counter(self.recipies['coffee_double'])
                    return 'Haciendo Café Doble'
                if self.election == 3:
                    self.resources = Counter(self.resources) - Counter(self.recipies['coffee_milk'])
                    return 'Haciendo Café con Leche'
                if self.election == 4:
                    self.resources = Counter(self.resources) - Counter(self.recipies['coffee_milk_double'])
                    return 'Haciendo Café Doble con Leche'
                if self.election == 5:
                    self.resources = Counter(self.resources) - Counter(self.recipies['capuccino'])
                    return 'Haciendo Capuchino'
                if self.election == 6:
                    self.resources = Counter(self.resources) - Counter(self.recipies['tea_simple'])
                    return 'Haciendo Té'   