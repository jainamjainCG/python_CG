balance = int(input("enter the account balance:"))
withdrawl = int(input("enter the withdrawl amount:"))

if withdrawl>0 and withdrawl%100==0 and withdrawl<balance and balance-withdrawl>=500:
    print("withdrawl successful")
else:
    ("enter the amount again")