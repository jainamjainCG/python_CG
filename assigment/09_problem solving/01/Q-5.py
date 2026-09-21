# Problem 5: Apply a 10% discount when the price is at least 1000.
#
# What is being asked? Calculate the final price after any applicable discount.
# Input: The item's price.
# Output: The final price.

price = float(input())

if price >= 1000:
    final_price = price * 0.90
else:
    final_price = price

print(final_price)
