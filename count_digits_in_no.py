"""
Write a python script to count digits in a given number
"""

# taking input from the user
num = int(input("Enter a number : "))

# defining digits variable to count digits of a given number
digits = 0

# counting digits of a number
while num != 0 :
    num //= 10
    digits += 1

# printing number of digit of a given number
print("Total number of digits are", digits)