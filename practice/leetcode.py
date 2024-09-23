#1. given a list, write a python program to swap the first and last elements in a list
swap_list = [12, 35, 9, 56, 24]

"""
1. Write a Python program to print the following string in a specific format (see the output).
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
Output :

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are!
"""
def poem():
    print("""
        Twinkle, twinkle, little star,\n
        \tHow I wonder what you are!\n
        \t\tUp above the world so high,\n
        \t\tLike a diamond in the sky.\n
        Twinkle, twinkle, little star,\n
        \tHow I wonder what you are!
        """
    )

# poem()#✅

"""2. Write a  Python program to find out what version of Python you are using."""
# Solution
def python_version():
    import sys
    print(f"My python version is: {sys.version} \n Here's my version info: {sys.version_info} \n Also my API version is: {sys.api_version}")

# python_version()#✅
    
"""3. Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14
"""
def current_date_and_time():
    import datetime
    current_date = datetime.datetime.now()
    print(f"""Current data and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}""")

# current_date_and_time()#✅

"""
4. Write a Python program that calculates the area of a circle based on the radius entered by the user.
Sample Output :
r = 1.1
Area = 3.8013271108436504
"""
def area_of_circle():
    from math import pi
    r = int(input("Pls input your radius: "))
    Area = pi*r**2
    print(f"Area = {Area}m2")
    # print(Area)
    return Area

area_of_circle()

""" 
5. Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
"""

def first_n_last_name():
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")

    my_name = [last_name, first_name]
    print(my_name[0] + " " + my_name[1])

# first_n_last_name()
    
"""
5. Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
"""

def first_and_last_name():
    first_name = input("What is your first name?")
    last_name = input("What is your last name?")
    print(f"{first_name} {last_name}")
    my_name = [last_name, first_name]
    
    print(" ".join(my_name))

# first_and_last_name()
    
"""
6. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""
# Solution
def list_tuple():
    sample_data = input("Please input your list: ")
    # sample_data = int(sample_data)
    List = sample_data.split(",")
    Tuple = tuple(List)
    print(
        f"""
        List : {List} \n
        Tuple : {Tuple}
        """
    )

list_tuple()

