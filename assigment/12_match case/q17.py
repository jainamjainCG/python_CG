type = int(input("enter 1 for saving account\nenter 2 for current acount\n:-"))
show = int(input("enter 1 for checking balance\nenter 2 for deposit\nenter 3 for withdraw\n:-"))
match type:
    case 1:
        match show:
            case 1:
                print("Saving Account\nChecking balance")
            case 2:
                print("Saving Account\nDepositing Money")
            case 3:
                print("Saving Account\nWithdrawing money")
            case _:
                print("invalid input")
    case 2:
        match show:
            case 1:
                print("Current Account\nChecking balance")
            case 2:
                print("Current Account\nDepositing Money")
            case 3:
                print("Current Account\nWithdrawing money")
            case _:
                print("invalid input")