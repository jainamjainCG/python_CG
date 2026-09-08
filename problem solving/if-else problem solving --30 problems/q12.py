character = input("enter the character:")

if character>=chr(97) and character<=chr(123):
    print("lowercase")
elif character>=chr(65) and character<=chr(91):
    print("uppercase")
elif character>=chr(33) and character<=chr(126):
    print("Special character")
elif character>=chr(48) and character<=chr(57):
    print("digits")
else:
    print("invalid")
