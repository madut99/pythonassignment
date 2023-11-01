import math

class Circle:
    def __init__(self, radius):

    def compute_area(self):
        # Formula for the area of a circle: A = π * r^2
        area = math.pi * (self.radius ** 2)
        return area
    def compute_perimeter(self):
         # Formula for the perimeter of a circle: P = 2 * π * r
        perimeter = 2 * math.pi * self.radius
        return perimeter
area = circle_instance.compute_area()
print(f"Area of the circle with radius {radius} is: {area}")

perimeter = circle_instance.compute_perimeter()
print(f"Perimeter of the circle with radius {radius} is: {perimeter}")
