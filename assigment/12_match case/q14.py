print("""
1 → Low
2 → Medium
3 → High
4 → Critical""")

priority = int("enter the number for level of problem customer have , at what level we should priotze the problem")

match priority:
    case 1|2:
        print("Normal priority")
    case 3|4:
        print("Urgent priority")
    case _:
        print("invalid input")