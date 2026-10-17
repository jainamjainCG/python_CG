print("""
1 → Electronics
2 → Clothing
3 → Books
4 → Grocery
5 → Exit""")

choice = int(input("Enter the store number: "))

match choice:
    case 1:
        print("Opening elctronics section")
    case 2:
        print("Opening clothing section")
    case 3:
        print("Opening the books section")
    case 4:
        print("Opening the grocery section")
    case 5:
        print("Exit")
    case _:
        print("Invalid choice")