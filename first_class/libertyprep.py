def listupler():
    values = input("Input some comma-separated numbers: ")
    list = values.split(",")
    tupler = tuple(list)
    print("List: ", list)
    print("Tuple: ", tupler)

# listupler()

def filename():
    file_name = input("what is your filename? ")
    split_name = file_name.split(".")

    print(split_name[1])

# filename()

def get_exam_date():
    exam_st_date = (11, 12, 2014)
    print("The examination will start from : %i / %i / %i" % exam_st_date)

# get_exam_date()

def print_colorlist():
    color_list = ["Red", "Green", "White", "Black"]
    print("%s %s" % (color_list[0], color_list[-1]))

# print_colorlist()

text = "IsEmpty"
# print(text[:2])
# print(text[2:])

# Functions
def printme(text):
    print(text)
    return

# printme("welcome to python functions")

# Function parameters
# *args and **kwargs
def myFun(*argv):
    for arg in argv:
        print(arg)

# myFun("Hello", "Welcome", "to", "GeeksforGeeks")
# myFun(1, 2, 3, 4, 5)

def myFun(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)

# myFun("Hello", "Welcome", "to", "GeeksforGeeks")

def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

# myFun(first="univelcity", mid="backend", last="development")

def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)

# myFun()

# How to Use *args and **kwargs in Python 
def multiply(x, y):
    print(x * y)

# multiply(37, 80)
# print(multiply(37, 80))

# multiply(2, 4, 5) # This throws an error because > 2 arguments were given

# Understanding *args
def multiply(*args):
    z = 1
    for num in args:
        z *= num
    print(z)

# multiply(4, 5)
# multiply(10, 9)
# multiply(2, 3, 4)
# multiply(3, 5, 10, 6)

a = 5
a *= 3
# print(a)

# Understanding **kwargs
def print_kwargs(**kwargs):
    print(kwargs)

# print_kwargs(kwargs_1="shark", kwargs_2=4.5, kwargs_3=True)
    
def print_values(**kwargs):
    for key, value in kwargs.items():
        # print("The value of {} is {}".format(key, value))
        print(f"The value of {key} is {value}")
        # print(f"The value of {value} is {key}")


print_values(my_name="Inie", your_name="Johnny Walker")

# **kwargs will take any number of arguments you pass in
# print_values(
#     name1="Alex",
#     name2="Bayo",
#     name3="Charles",
#     name4="David",
#     name5="Evelyn",
#     name6="Fola"
# )

# Using *args and **kwargs in function calls
def some_args(arg1, arg2, arg3, arg4):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)
    print("arg4:", arg4)

args = ("Sammy", "Casey", "Alex", True)
# some_args(*args)
my_list = [2, 4, 3]
# some_args(1, *my_list)

# Using keyworded arguments (**kwargs) to call a function
def some_kwargs(kwarg1, kwarg2, kwarg3):
    print("kwarg1", kwarg1)
    print("kwarg2", kwarg2)
    print("kwarg3", kwarg3)

kwargs = {"kwarg1": "Valerie", "kwarg2": "Harper", "kwarg3": "Remy Martin"}
# some_kwargs(**kwargs)