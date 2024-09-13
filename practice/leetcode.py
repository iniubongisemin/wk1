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
    

