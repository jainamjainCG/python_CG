# Problem 3: Calculate a rectangle's area and perimeter.
#
# What is being asked? Find both measurements from the rectangle's dimensions.
# Input: The length and width.
# Output: The area and perimeter.
# Conditions: None are stated.


length = float(input())
width = float(input())

area = length * width
perimeter = 2 * (length + width)

print("Area:", area)
print("Perimeter:", perimeter)
