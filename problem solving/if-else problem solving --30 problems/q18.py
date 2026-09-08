temp = int(input("enter the temperature in celsius:"))

if temp<0:
    print("Freezing")
elif temp<=0 and temp<=15:
    print("Very cold")
elif temp>=16 and temp<=25:
    print("Cold")
elif temp>=26 and temp<=35:
    print("Normal")
elif temp>=35:
    print("hot")
else:
    print("please enter the temperature again")