print("""Menu = 1 → Pizza
       2 → Burger
       3 → Pasta
       4 → Sandwich""")

choice = int(input("enter your choice: "))


match choice:
    case 1 :
        print("Pizza")
    case 2:
        print("burger")
    case 3:
        print("Pasta")
    case 4:
        print("sandwich")
    case _:
        print("Invalid Choice")