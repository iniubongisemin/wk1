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
7. Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java

"""

def print_file_extension():
    sample_file_name = input("Input your filename: ")
    Output = sample_file_name.split(".")
    print(f"Output : {Output[1]}")

# print_file_extension()

"""
8. Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
"""
def first_and_last_color():
    color_list = input("Provide your color list: ")
    colour_list = color_list.split(",")
    print(f"{colour_list[0]}, {colour_list[3]}")

first_and_last_color()
