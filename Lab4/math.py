import math

# 1. Write a Python program to convert degree to radian.
# Input degree: 15
# Output radian: 0.261904
def degree_to_radians():
  degree = int(input("Input degree: "))
  print("Output radian:", math.radians(degree))

# 2. Write a Python program to calculate the area of a trapezoid.
# Height: 5
# Base, first value: 5
# Base, second value: 6
# Expected Output: 27.5
def trapezoid_area():
  height = int(input("Height: "))
  first_value = int(input("Base, first value: "))
  second_value = int(input("Base, second value: "))
  print((first_value + second_value) / 2 * height)

# 3. Write a Python program to calculate the area of regular polygon.
# Input number of sides: 4
# Input the length of a side: 25
# The area of the polygon is: 625
def polygon_area():
  sides = int(input("Input number of sides: "))
  length = int(input("Input the length of a side: "))
  apothem = length / (2 * math.tan(math.radians(180) / sides))
  print(f"The area of the polygon is: {(sides * length * apothem) / 2}")

# 4. Write a Python program to calculate the area of a parallelogram.
# Length of base: 5
# Height of parallelogram: 6
# Expected Output: 30.0
def parallelogram_area():
  length = int(input("Length of base: "))
  height = int(input("Height of parallelogram: "))
  print(length * height)