num1 = int(input("enter the number1 :"))
num2 = int(input("enter the number2 :"))
operator = (input("enter the operator "))

if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/" and num2!=0:
    print(num1/num2)
else:
    print("enter the operator again")
    