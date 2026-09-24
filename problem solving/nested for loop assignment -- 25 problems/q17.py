num = int(input("enter a number :"))
for i in range(1,num,3):
    for j in range(i,i+3):
        print(j,end=" ")
    print()
