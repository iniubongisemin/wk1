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
    # print(f"{colour_list[0]}, {colour_list[3]}")
    pass 

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

# nth_factorial()


"""
11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.
"""
def builtin_functions():
    import builtins
    result = []
    for name in dir(builtins):
        obj = getattr(builtins, name)  
        if callable(obj):  
            result.append((name, obj.__doc__))  
    return result

# Print the result
for name, docstring in builtin_functions():
    # print(f"{name}:\n{docstring}\n")
    pass


"""
12. Write a  Python program to get the volume of a sphere with radius six.
Click me to see the sample solution
"""
def volume_of_sphere(r):
    from math import pi
    v = 4/3*pi*(r**3)
    v = round(v, 3)
    print(f"The volume of the sphere is: {v}m3")

# volume_of_sphere(10)

"""
13. Write a Python program that prints the calendar for a given month and year.
Note : Use 'calendar' module.
"""
def print_calendar():
    import calendar
    year_calendar = calendar.prcal(2024)
    month_calendar = calendar.month(2024, 10)
    print(year_calendar)
    print("\n\n")
    print(month_calendar)
    print("\n\n")

# print_calendar()
    
"""
13. Write a Python program to print the following 'here document'.
Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
"""
def print_heredoc():
    heredoc = """
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
"""
    # print(heredoc)

# print_heredoc()

"""
14. Write a Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
"""
def num_of_days():
    from datetime import datetime
    day_one = (2014, 7, 2)
    day_two = (2014, 7, 11)
    day_one = datetime(*day_one)
    day_one = day_one.strftime("%Y-%m-%d")
    day_one = datetime.strptime(day_one, "%Y-%m-%d")
    day_two = datetime(*day_two)
    day_two = day_two.strftime("%Y-%m-%d")
    day_two = datetime.strptime(day_two, "%Y-%m-%d")
    print(day_one)
    print(day_two)
    time_delta = day_two - day_one
    print(time_delta.days)
    
# num_of_days()
    
"""
15. Write a  Python program to get the volume of a sphere with radius six.
"""
def vol_of_sphere():
    from math import pi
    r = 6
    vol = 4/3*(pi*r**3)
    vol = int(vol)
    print("The vol of the sphere is: %xm3"% vol)

# vol_of_sphere()

"""
16. Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.
"""
def diff_btw_nums(n):
    abs_diff = abs(n-17)
    print(f"Absolute difference between {n} and 17 = {abs_diff}")
    if n > 17:
        print(f"Twice the absolute difference between {n} and 17 is: ", 2*abs_diff)
        return 2 * abs_diff
    
# diff_btw_nums(20)

"""
17. Write a Python program to test whether a number is within 100 of 1000 or 2000.
"""
def test_number_magnitude(num):
    if num in range(900, 1101):
        print("Number is within 100 of 1000")
    elif num in range(1900, 2101):
        print("Number is within 100 of 2000")
    else:
        print("Number is not in any of the ranges provided")

# test_number_magnitude(2030)

"""
18. Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
"""
def sum_equi_prod(x, y, z):
    if x==y==z:
        return 3*(x+y+z)
    else:
        return "The three numbers are not equal"

# print(sum_equi_prod(2, 2, 4))

"""
19. Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".
"""
def append_Is():
    str_ing = input("Please type in your string: ")
    if "Is" == str_ing[0:2]:
        return str_ing
    else:
        return "Is"+str_ing

# print(append_Is())

"""
20. Write a Python program that returns a string that is n (non-negative integer) copies of a given string.
"""
def n_copy(n):
    my_string = input("Please type any word 😊: ")
    return (my_string + " ")* n
    # for i in range(n):

# print(n_copy(10)) 

"""
21. Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.
"""
def odd_even():
    num = int(input("Enter a number: "))

    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

# odd_even()
        
"""
22. Write a Python program to count the number of occurences of 4 in a given list.
"""
my_list = [1, 4, 6, 4, 7, 4]
def freq_count(my_list:list):
    count = 0
    for num in my_list:
        if num == 4:
            count = count + 1
    return f"Number of occurences of 4 in my list = {count}"
    
# print(freq_count(my_list))

"""
23. Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2.
"""
def n_copies_of_string(n:int, str_ing:str):
    if len(str_ing) < 2:
        return (str_ing + " ") * n
    else:
        return (str_ing[0:2] + " ") * n
    
# print(n_copies_of_string(4, "ICUI4CU"))
    
"""
24. Write a Python program to test whether a passed letter is a vowel or not.
"""
def vowel_test(v:str):
    vowels = "aeiou"
    if v.lower() in vowels:
        return "Your letter is a vowel 😊"
    else:
        return "Your letter is a consonant 🤡"

# print(vowel_test("Y"))

"""
25. Write a Python program that checks whether a specified value is contained within a group of values.
"""
num_list = [1, 5, 8, 3]
def list_element(li_st:list, i):
    for number in li_st:
        if i == number:
            return True
    return False
        
# print(list_element(num_list, 3))

"""
26. Write a Python program to create a histogram from a given list of integers.
"""
li_st = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
li_sts = [11, 21, 31, 41, 51, 61, 71, 81, 91, 101]

# def histo_gram():
def histo_gram(list1:list, list2:list):
    import matplotlib.pyplot as plt 
    # import numpy as np # type: ignore
    # plt.hist(my_list, bins=10)

    # # plt.show()
    fig, ax = plt.subplots()             
    ax.plot(list1, list2)  
    plt.show()                           

print(histo_gram(li_st, li_sts))

    

