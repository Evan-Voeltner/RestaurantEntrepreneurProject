from logger import file_logger
from order_factory import OrderFactory

class Franchise:
    def __init__(self, location_number):
        self.location_number = location_number

    def place_order(self):
        print('What would you like to order?')
        print('Type 1 for Pizza, 2 for Pasta, 3 for Salad')
        user_input = input()
        
        desired_order = OrderFactory.create_order(user_input)
        file_logger.log_transaction(desired_order, self.location_number)
