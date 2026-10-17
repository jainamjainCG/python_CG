num = input("enter the number: ").split()
target = 7
flag = True
for i in num:
    if int(i)==target:
        flag=False
        print("Found")
        break
else:
    print("Not found")