# Taxicab.py

class Taxicab:
    """
    A class that represents a taxicab. It keeps track of its current 
    x and y coordinates on a grid, as well as an odometer reading that 
    tracks the total distance the taxicab has traveled.
    """

    def __init__(self, x_coord, y_coord):
        """
        Initializes the Taxicab object with a starting x-coordinate and 
        y-coordinate. The odometer is initialized to 0.
        """
        self._x_coord = x_coord
        self._y_coord = y_coord
        self._odometer = 0

    def get_x_coord(self):
        """
        Returns the current x-coordinate of the taxicab.
        """
        return self._x_coord

    def get_y_coord(self):
        """
        Returns the current y-coordinate of the taxicab.
        """
        return self._y_coord

    def get_odometer(self):
        """
        Returns the current odometer reading of the taxicab.
        """
        return self._odometer

    def move_x(self, distance):
        """
        Shifts the taxicab left or right by the specified distance. 
        Updates the x-coordinate and adds the absolute value of the 
        distance to the odometer.
        """
        self._x_coord += distance
        self._odometer += abs(distance)

    def move_y(self, distance):
        """
        Shifts the taxicab up or down by the specified distance. 
        Updates the y-coordinate and adds the absolute value of the 
        distance to the odometer.
        """
        self._y_coord += distance
        self._odometer += abs(distance)