num = int(input("enter a number :"))
for i in range(1,num,5):
    for j in range(i,i+5):
        print(j,end=" ")
    print()