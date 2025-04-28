from datetime import datetime
"""
7. File Extension Extractor
Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java
"""
def file_name_extractor():
    file_name = input("Please type your file name: ")
    output = file_name.split(".") 
    print("." + output[1])
    # split_file_name = file_name[-5:]
    # print(f"Output : {split_file_name}")
# file_name_extractor()

"""
8. First and Last Colors
Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White","Black"]
"""
def first_last_colors():
    color_list = ["Red","Green","White","Black"]
    print(color_list[0], color_list[-1])
# first_last_colors()

"""
9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
"""
"""
MORE PROBLEMS:
Write a Python program that takes a tuple of exam dates and prints them in "Month Day, Year" format.
Write a Python script that calculates how many days remain until an exam.
Write a Python program that extracts and prints only the year from an exam schedule tuple.
Write a script that takes multiple exam dates as input and prints the earliest one.
"""
def exam_date():
    exam_st_date = (11, 12, 2014)
    exams_date = f"{exam_st_date[0]} / {exam_st_date[1]} / {exam_st_date[2]}"
    # to_datetime = datetime.strptime(exams_date, "")
    print(exams_date)
    # print(f"The examination will start from : {exam_st_date[0]} / {exam_st_date[1]} / {exam_st_date[2]}")
    # print("The examination will start from : %a / %a / %a" % exam_st_date)

# exam_date()

"""
10. Number Expansion Calculator
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
"""
def number_expansion_calculator():
    n = int(input("Please type your number: "))
    num_exp = n+n**2+n**3
    print("The value of n is: ", num_exp)
# number_expansion_calculator()

"""
11. Function Documentation Printer
Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.
"""
def built_in_functions():
    import builtins
    result = []
    for name in dir(builtins):
        obj = getattr(builtins, name)
        if callable(obj):
            result.append((name, obj.__doc__))
            
    print(result)
    
# built_in_functions()

print(abs.__doc__)
    
"""
12. Monthly Calendar Display
Write a Python program that prints the calendar for a given month and year.
Note : Use 'calendar' module.
"""
def monthly_calendar():
    import calendar
    print(calendar.month(2025, 4))
# monthly_calendar()

"""
13. Multi-line Here Document
Write a Python program to print the following 'here document'.
Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
"""
def multi_line_doc():
    print(
    """
    a string that you "don't" have to escape
    This
    is a ....... multi-line
    heredoc string --------> example
    """
    )
# multi_line_doc()

"""
14. Days Between Dates
Write a Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
"""
date_one = (2014, 7, 2)
date_two = (2014, 7, 11)
def days_btw_dates(x, y):
    import datetime as dt
    
    # first_date = float(f"{x[0]/x[1]/x[2]}")
    # last_date = float(f"{y[0]/y[1]/y[2]}")
    # time_diff = dt.timedelta(hours=last_date)
    # time_delta = dt.timedelta(hours=first_date)
    # time_now = datetime.now()
    # first_equiv_time = time_now + time_diff 
    # last_equiv_time = time_now + time_delta
    # print("FIRST_DATE", first_equiv_time)
    # print("LAST_DATE", last_equiv_time)
    # # diff = datetime()
    # diff = last_equiv_time - first_equiv_time
    # print(f"Expected output : {diff}, DATATYPE::::{type(diff)}")

    first_date = dt.date(*x)
    second_date = dt.date(*y)
    delta = second_date - first_date
    print("SECOND_DATE>>>>>", second_date, "FIRST_DATE>>>>>", first_date)
    print(f"Expected output : {delta}")

# days_btw_dates(date_one, date_two)

"""
15. Sphere Volume Calculator
Write a Python program to get the volume of a sphere with radius six.
"""
def vol_of_sphere(r):
    from math import pi
    volume = 4/3*pi*r**3
    print(f"{int(volume)}cm3")

# vol_of_sphere(6)

"""
16. Difference from 17
Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.
"""
def diff_from_17(x:int):
    diff = x - 17 
    abs_diff = abs(x - 17) 
    print("ABS_DIFF>>>>>>>", abs_diff)
    if diff > 17:
        print(2*abs_diff)
        return 2*abs_diff
    else:
        print("X is not greater than 17!")
# diff_from_17(100)

"""
17. Number Range Tester
Write a Python program to test whether a number is within 100 of 1000 or 2000.
"""
def num_range_tester(x):
    if x in range(900, 1100):
        print("yes X is within 100 of 1000")
    elif x in range(1900, 2100):
        print("yes X is within 100 of 2000")

# num_range_tester(1001)

"""
18. Triple Sum Calculator
Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
"""
def triple_sum_calculator(x, y, z):
    summ=x+y+z
    if x==y==z:
        print("The values are equal", 3*summ)
        return 3*summ
    else:
        print("The values are not equal")
# triple_sum_calculator(1,1,1)

"""
19. Prefix "Is" String Modifier
Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".
"""
def prefix_is(stringg:str):
    if stringg[:2] == "Is":
        print(stringg[:2])
        print(stringg)
    else:
        print("Is"+stringg)
prefix_is("abella")