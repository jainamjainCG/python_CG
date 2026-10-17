print('''
1 → View Profile
2 → View Courses
3 → View Marks
4 → View Attendance
5 → Logout''')

choice = int(input("what you wanna do: "))

match choice:
    case 1:
        print("Opening your Profile")
    case 2:
        print("Opening the course details")
    case 3:
        print("Opening Marks")
    case 4:
        print("Opening your Attendance")
    case 5:
        print("Logout")
    case _:
        print("Invalid choice")
        