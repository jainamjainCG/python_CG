num =input("enter the marks: ").split()

for i in num:
    if int(i)<40:
        continue
    print(i,end=" ")