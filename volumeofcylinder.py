import math

# Prompt the user to enter the radius and height of the cylinder.
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

# Calculate the volume of the cylinder.
volume = math.pi * radius * radius * height

# Print the volume of the cylinder.
print("The volume of the cylinder is:", volume)
