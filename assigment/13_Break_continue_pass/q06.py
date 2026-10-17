num = input("enter the numbers: ").split()
for i in num:
    if int(i)<0:
        break
    print(i,end="")