purchase = int(input("enter your purchase amount:"))

if purchase<500:
    print("no discount")
elif purchase>=500 and purchase<999:
    print(f"congratulation! you got 5% discount, your total bill is= {purchase-(purchase/100)*5}")
elif purchase>=1000 and purchase<1999:
    print(f"congratulation! you got 10% discount, your total bill is= {purchase-(purchase/100)*10}")
elif purchase>=2000 and purchase<4999:
    print(f"congratulation! you got 15% discount, your total bill is {purchase-(purchase/100)*15}")
elif purchase>5000:
    print(f"congratulation! you got 20% discount, your total bill is {purchase-(purchase/100)*20}")
else:
    print("invalid purchasing")