number1 = int(input("enter a number1 :"))
number2 = int(input("enter a number2 :"))
number3 = int(input("enter a number3 :"))

if number1>number2 and number1>number3:
    print("number1 is largest")
elif number2>number3 and number2>number1:
    print("number2 is largest")
elif number3>number1 and number3>number2:
    print("number3 is largest")
else:
    print("all numbers are equal")