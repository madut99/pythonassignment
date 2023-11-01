class Rectangle:
    ("A class to represent a rectangle and compute its area and perimeter.")

    def __init__(self, length, width):
        ("Initializes a new Rectangle object with the given length and width.")
        self.length = length
        self.width = width

    def computeArea(self):
        ("Computes the area of the Rectangle object.")
        area = self.length * self.width
        print("area")

    def computePerimeter(self):
        ("Computes the perimeter of the Rectangle object.")
        perimeter = 2 * (self.length + self.width)
        print("perimeter")
