marks = int(input("enter the marks :"))

if marks<0 or marks>100:
    print("marks are invalid")
elif marks>=40:
    print("pass")
else:
    print("fail")