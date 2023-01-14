"""
Write a python script to print binary equivalent of a given decimal number
(Do not use bin() method)
"""

# taking input from the user
num = int(input("Enter a number : "))
temp = num

# defining binary_num variable to store binary of given number
binary_num = str()

# flag variable to set False if the number is negative
num_positive = True

# checking whether the given number is positive or negative
if num < 0 :
    num = -num
    num_positive = False

# getting binary equivalent of given decimal number
while num != 0 :
    binary_num += str(num%2)
    num //= 2

# adding prefix '0b' to represent binary number
if num_positive is True :
    if temp == 0 :
        binary_num += '0b0'
    else :
        binary_num += 'b0'
else :
    binary_num += 'b0-'

# reversing the binary_num string
binary_num = binary_num[::-1]

# printing binary equivalent of the given decimal number
print("Binary --> \'%s\'" %(binary_num))