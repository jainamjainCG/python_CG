str =input("enter a word: ")
target = "p"
flag = True
for i in str:
    if i==target:
        flag=False
        print("found")
        break
else:
    print("not found")