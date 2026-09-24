num = int(input("enter a number :"))
for i in range(1,num+1):
    for j in range(1,11):
        print(f"{i}*{j}={i*j}",end="  ")
    print()