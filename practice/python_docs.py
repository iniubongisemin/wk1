"""
To declare an encoding other than the default one, a special comment line should be added as the first line of the file.
# -*- coding: encoding -*-
"""

"""
CASTING: Since Python is an OOL, it uses classes to define data types. This is done using constructor functions e.g 
int()
float()
str()
"""
# e.g 
# print(int(32.88)) # = 32

"""
Get the characters from the start to position 5 (not included):
"""

b = "Hello, World!"
# print(b[:5])

"""
Get the characters from position 2, and all the way to the end:
"""
b = "Hello, World!"
# print(b[2:])

"""
Unpack a Collection
If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
"""
# E.g 
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

# print(x)
# print(y)
# print(z)

"""
21. Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.
"""
def even_or_odd():
    num = int(input("Please type in a number: "))
    if num % 2 == 0:
        print("Your number is an even number")
    else:
        print("Your number is an odd number")

# even_or_odd()
        
"""
20. Write a Python program that returns a string that is n (non-negative integer) copies of a given string.
"""
def n_copies_of_string(n):
    my_string = "string"
    return n * (my_string + " ")

print(n_copies_of_string(10))