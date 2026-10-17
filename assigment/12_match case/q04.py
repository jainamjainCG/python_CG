signal = input("enter the colout of traffic signal light: ").lower().strip()

match signal:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("GOO")
    case _:
        print("invalid Signal")