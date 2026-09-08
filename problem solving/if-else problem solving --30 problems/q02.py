number = int(input("enter a number :"))
if number>0 and number%2==0:
    print("Positive even")
elif number<0 and number%2!=0:
    print("Positive odd")
elif number<0 and number%2==0:
    print("Negative even")
elif number<0 and number%2!=0:
    print("Negative odd")
else:
    print("zero")
    