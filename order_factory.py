from order import Order
from pizza import Pizza
from pasta import Pasta
from salad import Salad

class OrderFactory:
    def __init__(self):
        pass

    @staticmethod
    def create_order(desired_dish):
        if desired_dish == 'salad':
            return Salad()
        elif desired_dish == 'pasta':
            return Pasta()
        elif desired_dish == 'pizza':
            return Pizza()
        else:
            print(f'{desired_dish} is not a dish')