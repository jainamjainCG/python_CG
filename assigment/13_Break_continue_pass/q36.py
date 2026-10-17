num = input("enter the number for range: ").split()
target = 9

for i in num:
    if int(i)<=0:
        continue
    elif int(i)==target:
        print("Target found")
        break

else:
    print("target not found")
