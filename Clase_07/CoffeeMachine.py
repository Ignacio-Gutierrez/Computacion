import unittest


class CoffeeMachine:
    def __init__(self):
        self.coins = 0

    def insert_coin(self):
        self.coins += 1


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