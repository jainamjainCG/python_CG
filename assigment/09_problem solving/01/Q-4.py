# Problem 4: Classify a number as positive, negative, or zero.
#
# What is being asked? Determine the number's sign.
# Input: One number.
# Output: positive, negative, or zero.

number = float(input())

if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")
