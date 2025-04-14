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
monthly_calendar()

