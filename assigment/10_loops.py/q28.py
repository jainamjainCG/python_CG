num = int(input("enter a number :"))

for i in range(1,num):
    for j in range(i):
        print("*",end="")
    print()