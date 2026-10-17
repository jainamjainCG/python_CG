wheather = input("enter the condition of wheather")

match wheather:
    case 1:
        print("The wheather is sunny outside , so , wear sunglasses")
    case 2:
        print("the wheather is rainy outside please carry an umbrella today")
    case 3:
        print("The wheather is cloudy outside , wheather may change today")
    case 4:
        print("The wheather is snowy outside , please wear warm cloths today")
    case _:
        print("Invalid Wheather Report")