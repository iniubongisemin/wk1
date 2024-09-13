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
3. Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14
"""
# Solution
def current_date_and_time():
    import datetime
    current_date_time = datetime.datetime.now()
    print(
        f"""Current date and time :\n{current_date_time.strftime("%Y-%m-%d %H:%M:%S")}
        """
    )
# current_date_and_time()

"""
Get the characters from the start to position 5 (not included):
"""

b = "Hello, World!"
print(b[:5])

"""
Get the characters from position 2, and all the way to the end:
"""
b = "Hello, World!"
print(b[2:])