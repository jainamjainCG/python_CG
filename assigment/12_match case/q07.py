print('''
1 → Account Balance
2 → Mini Statement
3 → Fund Transfer
4 → Bill Payment
5 → Customer Support''')

choice = int(input("enter the service you need"))

match choice:
    case 1:
        print("Checking Account Balance")
    case 2:
        print("Checking Mini Statement")
    case 3:
        print("Transfering Fund")
    case 4:
        print("Opening Bill Payment Section")
    case 5:
        print("Connecting Customer Support")