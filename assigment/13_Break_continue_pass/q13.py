str = input("enter a wword/name: ")
ch = input("enter a single word only: ")
chr=ch[0]

for i in str:
    if i==chr:
        continue
    print(i,end="")