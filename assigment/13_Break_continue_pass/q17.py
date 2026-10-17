str = input("enter a word: ").lower()


for i in str:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        continue
    print(i,end="")
