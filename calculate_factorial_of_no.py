"""
Write a python script to calculate factorial of a given number
"""

# taking input from the user
num = int(input("Enter a number : "))

# defining factorial variable to store factorial of a given number
factorial = 1

# defining i variable for iteration
i = 1

# calculating factorial of a given number
while i <= num :
    factorial *= i
    i += 1

# printing factorial of a given number
print("Factorial of %d is %d" %(num, factorial))
