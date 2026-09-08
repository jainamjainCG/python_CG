character = input("enter the character:")
Vowels=chr(97) or character==chr(101) or character==chr(105) or character==chr(111) or character==chr(117)

if character==chr(97) or character==chr(101) or character==chr(105) or character==chr(111) or character==chr(117):
    print("character is Vowel")
elif character>=chr(97) and character<=(123) and character!=Vowels:
    print("character is consonents")
else:
    print("invalid character")