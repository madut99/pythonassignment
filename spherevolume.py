import math
def calculate_sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)
radius = float(input("Enter the radius of the sphere: "))
volume = calculate_sphere_volume(radius)
print(f"The volume of the sphere with radius {radius} units is {volume:.2f} cubic units.")



