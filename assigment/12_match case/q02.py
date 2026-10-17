print("""settings:-
1 → Wi-Fi
2 → Bluetooth
3 → Mobile Data
4 → Airplane Mode
5 → Exit""")

choice = int(input("enter the number which you want to open: "))

match choice: 
    case 1:
        print("Wi-Fi")
    case 2:
        print("Bluetooth")
    case 3:
        print("Mobile Data")
    case 4:
        print("Airplane Mode")
    case 5:
        print("Exit")
    case _:
        print("Invalid Setting")