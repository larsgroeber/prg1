"""Solution for exercise 6.3."""


class Bike:
    """Class which defines a bike."""

    def __init__(self):
        # mileage is a number
        self.mileage = 0
        # age is a number
        self.age = 0
        # color is a string
        self.color = 'invisible'
        # brand is a string
        self.brand = 'bike'

    def set_color(self, color):
        """
        Sets the color for this bike.
        :param color: The new color
        """
        self.color = color
        print('You changed the color to', color)

    def show_color(self):
        """
        Prints the current color.
        """
        print('This bike is', self.color)

    def inc_miles(self):
        """
        Increments mileage by one.
        """
        self.mileage += 1


class EBike(Bike):
    """Class which defines an E-Bike."""

    def __init__(self, capacity, consumption):
        super().__init__()
        self.capacity = capacity
        self.consumption = consumption  # capacity per mile

    def show_reach(self):
        """
        Prints the remaining miles.
        """
        print('This ebike can go', self.capacity / self.consumption, 'miles.')


def main():
    bike1 = Bike()
    bike2 = Bike()
    bike1.set_color('red')
    bike2.set_color('blue')
    bike1.inc_miles()
    bike1.inc_miles()
    bike2.inc_miles()

    ebike1 = EBike(100, 2)
    ebike2 = EBike(210, 3)
    ebike1.show_reach()
    ebike2.show_reach()
    help(ebike1)


if __name__ == '__main__':
    main()
