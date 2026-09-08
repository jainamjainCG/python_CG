number1 = int(input("enter a number1 :"))

if number1%3==0:
    print("number1 is divisible by 3")
elif number1%7==0:
    print("number1 is divisible by 7")
elif number1%3==0 and number1%7==0:
    print("number1 is divisible by both number")
else:
    print("number1 is divisible by neither 3 nor 7")