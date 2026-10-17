food=int(input("enter 1 if you are vegetarian\nenter 2 if you are non-vegetarian\n:-"))
veg =int(input("enter 1 to order panner\nenter 2 to order dal\nenter 3 to order veg-biriyani\n:-")) 
non_veg= int (input("enter 1 to order chicken curry\nenter 2 to order chicken biriyani\nenter 3 to order fish fry\n:-"))

match food:
    case 1:
        match veg:
            case 1:
                print("panner ordered")
            case 2:
                print("dal ordered")
            case 3:
                print("veg-biriyani ordered")
            case _:
                print("Not available")
    case 2:
        match non_veg:
            case 1:
                print("chicken curry ordered")
            case 2:
                print("chicken biriyani ordered")
            case 3:
                print("fish fry ordered") 
            case _:
                print("Not available")
    case _:
        print("explain again please")