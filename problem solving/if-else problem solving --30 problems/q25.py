sub1 = int(input("enter the marks of sub1 :"))
sub2 = int(input("enter the marks of sub2 :"))
sub3 = int(input("enter the marks of sub3 :"))
average = (sub1+sub2+sub3)/3
if sub1==sub2==sub3>0 or sub1==sub2==sub3<100 :
    if sub1==sub2==sub3>=35:
        if average>=75:
            print("Distinction")
        if average>=60 and average<75:
            print("First class")
        if average>=50 and average<60:
            print("Second class")
        if average>=35 and average<50:
            print("pass")
    if sub1<35 or sub2<35 or sub3<35:
        print("Fail")
else:
    print("invalid marks")