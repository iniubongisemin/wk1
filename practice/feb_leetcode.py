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

date_time_display()
