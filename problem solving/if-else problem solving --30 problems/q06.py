number1 = int(input("enter a number1 :"))

if number1%10==5 or number1%10==0:
    print("number1 is divisible by 5")
elif number1%11==0:
    print("number1 is divisible by 11")
elif number1%5==0 and number1%11==0:
    print("number1 is divisible by both number")
else:
    print("number1 is divisible by neither 5 nor 11")