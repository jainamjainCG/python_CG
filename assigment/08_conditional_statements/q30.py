age = int(input("enter your age:"))
marks = int(input("enter your marks:"))
has_id = int(input("do you have id True/False:"))

if age>=18 and marks>=40 and has_id==True:
    print("Eligible")
else:
    print("not eligible")