"""
Write a python script to print octal equivalent of a given decimal number
(Do not use oct() method)
"""

# taking input from the user
num = int(input("Enter a number : "))
temp = num

# defining octal_num variable to store octal of given number
octal_num = str()

# flag variable to set False if the number is negative
num_positive = True

# checking whether the given number is positive or negative
if num < 0 :
    num = -num
    num_positive = False

# getting octal equivalent of given decimal number
while num != 0 :
    octal_num += str(num%8)
    num //= 8

# adding prefix '0b' to represent binary number
if num_positive is True :
    if temp == 0 :
        octal_num += '0o0'
    else :
        octal_num += 'o0'
else :
    octal_num += 'o0-'
  
# reversing the octal_num string
octal_num = octal_num[::-1]
# printing octal equivalent of the given decimal number
print("octal --> \'%s\'" %(octal_num))