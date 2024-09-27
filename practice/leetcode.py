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

# area_of_circle()

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

# list_tuple()

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

# first_and_last_color()

"""
9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
"""

def extract_exam_date(): 
    exam_st_date = (11, 12, 2014)
    # day = exam_st_date[0]
    # month = exam_st_date[1]
    # year = exam_st_date[2]
    # print(f"The examination will start from : {day} / {month} / {year}")
    print(f"The examination will start from : %a / %a / %a" % exam_st_date)

# extract_exam_date()
    
"""
10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
"""
def nth_factorial():
    n = (input("Please input a number: "))
    str_n = str(n)
    str_nn = str(n*2)
    str_nnn = str(n*3)
    nth_factor_ial = int(str_n)+int(str_nn)+int(str_nnn)

    print(nth_factor_ial)
    
    return nth_factor_ial

nth_factorial()