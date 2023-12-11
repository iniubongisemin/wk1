name = "inie"
name2 = "ubong"
_names = "iniubong isemin"
counter =  100
_count = 100
name1 = "Utom"

# Datatypes 
# Numeric: int, float, complex e.g 500, 4.5, pi
# String: str e.g "univelcity"
# Sequence: list, tuple, range
# Binary: bytes, bytearray, memoryview
# Mapping: dict
# Boolean: bool e.g True or False  
# Set: set, frozenset
# None: NoneType

# print(type(22))
# print(type(True))
# print(type(None))

# You can store datatypes in variables e.g
# is_student = True
# print(type(is_student))

# container data type
# tuple_sam = () 
# diction = {} 
# sample_list = []
# print(type(tuple_sam))
# print(type(diction))
# print(type(sample_list))

# functions 
# program to request input from users 
student_name = input("what is your name? ")
student_email = input("what is your email address? ")
student_age = input("how old are you? ")
print(student_name)
print(student_email)
print(student_age)

# string formatting using f - string 
# print(f"{student_name} - {student_email} - {student_age}")

# converting input to specific data types 
test_val = "20"
intelligent_ini = "True"
a = 20
new_val = int(test_val)
fun = bool(intelligent_ini)
conv = float(test_val)
b = str(a)
print(type(test_val))
print(type(new_val))
print(type(fun))
print(type(intelligent_ini))
print(type(conv))

print(f"my name is {student_name} you can reach me via {student_email}, I am {student_age} years old") 