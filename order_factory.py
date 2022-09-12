from pizza import Pizza
from pasta import Pasta
from bangbang import Salad

class OrderFactory:
    def __init__(self):
        pass

    @staticmethod
    def create_order(desired_dish):
        if desired_dish == '1':
            return Pizza()
        elif desired_dish == '2':
            return Pasta()
        elif desired_dish == '3':
            return Salad()
        else:
            print(f'{desired_dish} is not a dish')