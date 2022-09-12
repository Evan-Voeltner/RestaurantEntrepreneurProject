from order import Order

class Pizza(Order):
    def __init__(self):
        super().__init__()
        self.name = 'Pizza'
        self.price = 15