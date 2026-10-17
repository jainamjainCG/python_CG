print("""
4.upi
3.card
2.cash
1.wallet""")

choice = int(input("enter the payment method: "))

match choice:
    case 1:
        print("UPI payment Selected")
    case 2:
        print("Card payment selected")
    case 3:
        print("Cash payment selected")
    case 4:
        print("Wallet payment selected")
    case _:
        print("Invalid payment mode")