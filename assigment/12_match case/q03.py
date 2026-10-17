print("""
1 → Check Balance
2 → Withdraw Money
3 → Deposit Money
4 → Change PIN
5 → Exit""")

choice = int(input("enter the service you need: "))

match choice:
    case 1:
        print("Check Balance")
    case 2:
        print("Withdraw Money")
    case 3:
        print("Deposit Money")
    case 4:
        print("Change PIN")
    case 5:
        print("Exit")
    case _:
        print("Invalid Choice")