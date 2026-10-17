int = int(input("enter the number: "))

for i in range(2,int):
    if int%i==0:
        print("Not prime")
        break
else:
    print("Prime")