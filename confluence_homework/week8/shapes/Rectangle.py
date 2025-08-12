from Shape import Shape

class Rectangle(Shape):
    """
    A class representing a rectangle, inheriting from Shape.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """

    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
    
    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            float: The area computed as width x height.
        """
        return self.width * self.height
    

    

