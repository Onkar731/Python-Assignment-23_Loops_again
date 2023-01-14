"""
Write a python script to calculate sum of digits of a given number
"""

# taking input from the user
num = int(input("Enter a number : "))

# defining sum variable to store sum of digits of a given number
sum = 0

# calculating sum of digits of given number
while num != 0 :
    sum += num%10
    num //= 10

# printing sum of digits
print("Sum of digits is", sum)