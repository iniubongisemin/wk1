"""
1. Write a Python program to print the following string in a specific format (see the output).
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
Output :

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
"""
poem = "Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are"
# print(poem)

"""
2. Write a Python program to find out what version of Python you are using.
"""
def python_version():
    from sys import version
    print(f"My Python version is: {version}")
# python_version()

"""
3. Current DateTime Display
Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14
"""
def date_time_display():
    from datetime import datetime
    print(f"Current date and time: \n{datetime.now().replace(microsecond=0)}")

# date_time_display()

"""
4. Circle Area Calculator
Write a Python program that calculates the area of a circle based on the radius entered by the user.
Sample Output :
r = 1.1
Area = 3.8013271108436504
"""
def area_of_circle():
    from math import pi
    r = float(input(f"Please input the radius of your circle: "))
    area = pi*r**2
    print(f"Area = {area}")
# area_of_circle()

"""
5. Reverse Full Name
Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
"""
def name_reversor():
    name = input("What is your name? ")
    output = name.split(" ")
    reversed_name = output[1] + " " + output[0]
    print(reversed_name)
# name_reversor()

"""
6. List and Tuple Generator
Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""
def list_tuple_generator():
    sample_data = input("Please provide a sequence of numbers: ")
    split_data = sample_data.split(", ")
    # list_data = [sample_data]
    # tuple_data = (i for i in split_data)
    tuple_data = tuple(sample_data[0:])
    print(f"List : {split_data} \nTuple : {tuple_data} ")

list_tuple_generator()

