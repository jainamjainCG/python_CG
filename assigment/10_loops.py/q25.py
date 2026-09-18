str = input("enter a name :")
count = 0
for i in str:
    if i>=chr(65) and i<=chr(90):
        count = count+1
print(count)