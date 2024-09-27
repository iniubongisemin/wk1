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

