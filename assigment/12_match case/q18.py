choose = int(input("enter 1 to go to the electronics store\nenter 2 to go to the clothing store"))
electronics = int(input("enter 1 to purchase Mobile\nenter 2 to purchase Laptop\nenter 3 to purchase Headphone\n:-"))
clothing = int(input("enter 1 to purchase Shirt\nenter 2 to purchase Jeans\nenter 3 to purchase Shoes\n:-"))

match choose:
    case 1:
        match electronics:
            case 1:
                print("Mobile purchased")
            case 2:
                print("Laptop purchased")
            case 3:
                print("Headphone purchased")
            case _:
                print("out of stock , choose another item")
    case 2:
        match clothing:
            case 1:
                print("Shirt purchased")
            case 2:
                print("Jeans purchased")
            case 3:
                print("Shoes purchased")
            case _:
                print("out of stock, choosse another style")
    case _:
        print("invalid")