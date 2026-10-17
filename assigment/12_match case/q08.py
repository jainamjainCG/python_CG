print('''
1 → Morning Show
2 → Afternoon Show
3 → Evening Show
4 → Night Show''')

choice = int(input("Enter the show time you want to book"))

match choice:
    case 1:
        print("Booking Morning Show")
    case 2:
        print("Booking Afternoon Show")
    case 3:
        print("Booking Evening Show")
    case 4:
        print("Booking Night Show")
    case _:
        print("Invalid Booking")