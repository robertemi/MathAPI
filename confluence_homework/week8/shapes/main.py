from Rectangle import Rectangle
from Circle import Circle

def main():
    circle = Circle(3)
    rectangle = Rectangle(3, 4)

    # print(circle.area.__doc__)
    # print(rectangle.area.__doc__)

    c1 = Circle(4)
    c2 = Circle(2)
    c3 = Circle(5)
    c4 = Circle(9)

    r1 = Rectangle(4, 5)
    r2 = Rectangle(2, 4)
    r3 = Rectangle(5, 8)
    r4 = Rectangle(2, 7)

    shapes = [c1, c2, c3, c4, r1, r2, r3, r4]

    counter_rects = 0
    counter_circles = 0
    for shape in shapes:
        if isinstance(shape, Rectangle):
            counter_rects += 1
        elif isinstance(shape, Circle):
            counter_circles += 1
        print(shape.area())
    
    print(f'Circles: {counter_circles}')
    print(f'Rectangles: {counter_rects}')

main()