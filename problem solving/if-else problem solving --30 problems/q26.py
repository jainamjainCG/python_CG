day = int(input("enter the day"))
month = int(input("enter the month"))
year = int(input("enter the year"))

if day>0 and day<32 and month>0 and month<13 and month==1==3==5==7==8==10==12 and year>0:
    print(f"{day}/{month}/{year}")
elif day>0 and day<31 and month>00 and month<13 and month==4==6==9==11 and year>0:
    print(f"{day}/{month}/{year}")
elif day>0 and day<29 and month==2 and year>0:
        print(f"{day}/{month}/{year}")
elif day>0 and day<30 and month==2 and year>0:
    if year%400==0:
        print(f"{day}/{month}/{year}")
    elif year%4==0 and year%100!=0:
        print(f"{day}/{month}/{year}")
    else:
        print("invalid")
else:
    print("invalid")
