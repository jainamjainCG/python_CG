select = int(input("enter 1 if you are student \nenter 2 if you are teacher \n:-"))

if select==1:
    menu = int(input("enter 1 to view course\nenter 2 to view marks\nenter 3 to view attendance\n:-"))
    match menu:
        case 1:
            print("showing your course")
        case 2:
            print("showing your marks")
        case 3:
            print("showing attendance")
        case _:
            print("invalid input")

elif select==2:
    menu = int(input("enter 1 to view student \nenter 2 to enter student marks\nenter 3 to view attendance\n:- "))
    match menu:
        case 1:
            print("viewing student details")
        case 2:
            print("enter the marks")
        case 3:
            print("viewing attendance")
        case _:
            print("invalid input")

else:
    print("invalid input")