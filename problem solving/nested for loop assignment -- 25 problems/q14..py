num = int(input("enter a number :"))
for i in range(2,num+2,2):
    for j in range(2,i,2):
        print(j,end=" ")
    print()