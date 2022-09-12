from order import Order

class Pasta(Order):
    def __init__(self):
        super().__init__()
        self.name = 'Pasta'
        self.price = 10