str = input("enter the word: ").lower()
chr="r"
for i in str:
    if i==chr:
        print("Character exist")
        break
else:
    print("Character missing")