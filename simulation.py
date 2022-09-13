from franchise import Franchise

class Simulation:
    def __init__(self):
        pass

    def run_simulation(self):
        franchise_one = Franchise(1)
        franchise_two = Franchise(2)
        franchise_three = Franchise(3)
        for _ in range(3):
            franchise_one.place_order()
        for _ in range(3):
            franchise_two.place_order()
        for _ in range(3):
            franchise_three.place_order()