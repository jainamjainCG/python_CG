side1 = int(input("enter the side1 of triangle:"))
side2 = int(input("enter the side2 of triangle:"))
side3 = int(input("enter the side3 of triangle:"))

if side1+side2>side3 or side2+side3>side1 or side1+side3>side2:
    if side1==side2==side3:
        print("it is an equilateral triangle")
    if side1==side2!=side3 or side2==side3!=side1 or side1==side3!=side2:
        print("it is an isosceles triangle")
    if side1!=side2!=side3:
        print("it's a Scalene triangle")