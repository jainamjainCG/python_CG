num = int(input("enter a number :"))
for i in range(0,num+1,2):
    for j in range(1,i,2):
        print(j,end=" ")
    print()