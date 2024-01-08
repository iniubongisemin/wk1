# python collections (arrays)
#1. list: a collection which ordered, changeable, and allows duplicate members
#2. tuple: ordered, unchangeable and allows duplicates
#3. set: unordered, unchangeable(but you can remove and/or add items whenever you like), unindexed and doesn't allow duplicates 
#4. dictionary: ordered, changeable and doesn't allow duplicate members 
# NB: always choose the appropriate collection for a given data set as it impacts on the efficiency, retention/loss of meaning and security

# list collection type
name_list = ["inie", "james", "john", "henry", "sandra"]
new_name = ["emma", "sam", "joe"] 
# print(type(name_list))
# print(type(new_name))

# accessing values in a list
print("john" in name_list)
print(name_list + new_name)
print(name_list[0])
print(name_list[0:2])
print(len(name_list))
name_list[0] = "tracy"
print(name_list)
name_list[4] = "iniubong"
print(name_list)
del name_list[-1]  # deleting items
print(name_list)   

name_list.append("harrison")
name_list.insert(1, "faith")
# print(name_list)
name_list.remove('sandra')
print(name_list)

# first program
# input to receive a name from a user and put the name into your list
attendance = ["peter", "james", "john"]
# name = input("enter your name: ")
# attendance.append(name)
# print(attendance)

# tuples in python
student_tuple = ("henry", "james", "john", 10, 9, 7)
# print(student_tuple)
# print(student_tuple[0])
# print(student_tuple[0:2]) 
# using count tuple method 
# print(student_tuple.count("henry"))
# using index tuple method 
# print(student_tuple.index("james"))
# converting from tuple to list
student = list(student_tuple)
# student[0] = "sam"
# print(student)
student_tuple = tuple(student)
# student_tuple[0]  = "sam"
# print(student_tuple)

# converting data structures 
list()
tuple()
dict()

# exercises 
complex_list = [["john", 19, 'iceley007@gmail.com'], 200, 'class_d', [20, 24, 19]]
print(complex_list[0][-1])
print(len(complex_list))

