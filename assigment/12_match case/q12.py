print("""
admin
teacher
student
guest""")

choose = input("enter your role from given above: ").lower().strip()

match choose:
    case "admin":
        print("you have full access")
    case "teacher":
        print("opening teacher dashboard")
    case "student":
        print("student dashboard")
    case "guest":
        print("limited access")
    case _:
        print("invalid access")