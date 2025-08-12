from Shape import Shape
import math

class Circle(Shape):
    """
    A class representing a circle, inheriting from Shape.

    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area computed using πr².
        """
        return math.pi * self.radius ** 2 

c = Circle(2)
print(type(c))