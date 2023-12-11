# Python Data Type Conversion 
# Conversion to int, float and string
# Conversion to int
a = int(1)      # a will be 1
b = int(2.2)    # b will be 2 
c = int("3")    # c will be 3

# print(type(a))
# print(type(b))
# print(type(c))
         
# Conversion to float
d = float(1)        # d will be 1.0
e = float(2.2)      # e will be 2.2
f = float("3.3")    # f will be 3.3

# print(type(d))
# print(type(e))
# print(type(f))

# Conversion to string
g = str(1)          # g will be "1"
h = str(2.2)        # h will be "2.2"
i = str("3.3")      # i will be "3.3"

# print(h)
# print(i)
# print(type(h))
# print(type(i))

# Arithmetic Operators
# Addition +
# Subtraction -
# Multiplication *
# Division /
# Modulus %
# Exponentiation **
# Floor division //
# print(5 + 5)
# print(5 - 5)
# print(9 / 4)
# print(9 // 4)     # returns the whole number and disposes the remainder
# print(10 ** 2)    # returns the square 
# print(10 % 2)     # returns the remainder after division 

# comparison Operators: They return "True or False"
# == equal 
# != is not equal 
# > greater than 
# < less than 
# >= greater than or equal to 
# <= less than or equal to 
# print(5 == 5)
# print(7 == 4)
# print(10 < 6)
# print(9 > 6)
integ = 5
# print(type(integ))
# print(integ is 5) 

num2 = 10
name1 = "inie"
name2 = "univelcity"
# name = input("enter your name: ")
name = name1
# print(name1 is name)

# Logical Operators 
# They're used to combine conditional statements
# and: returns true only when the two statements are correct
# or: returns true if one of the statements are true
# not: reverses the result, return false if the result is true

 # Identity Operators 
 # They compare objects to see if they are actually the same object within the sample memory location
 # is: returns true if both variables are the same object
 # is not: returns true if both variables are not the same object

# String Methods
message = "welcome to python for beginners"
# print(message[0])
# print(message[1:5])
school = "univelcity"   
bootcamp = "welcome to univelcity"         
# print(school[0])
# print(school[0:6])  
# print(school[3:])
# print(school[-1])
# print(bootcamp[-3:])
# print(school[::-3])
# print(bootcamp[3:])
# print(len(school))
# print(len(bootcamp))

j = "hello"
k = "python"
print(j[1:4]) # Range Slice
print(j + k) # Concatenation
print(j * 2) # Repetition
print(k[-1]) # Slice

# String Formatting
#1 Using the string formatting operator i.e %modulo
# print("My name is %s and I weigh %d kg" %('Inie', 60))
# print("There are %d dogs" %10)
# print("I own %d dogs" %50)
# print("Univelcity's course completion rate is %f" %75.0)

#2 Formatting String using format() Method
# They work by putting in one or more replacement fields and placeholders defined by a pair of curly braces {} into a string and calling the str.format()
# The value we wish to put into the placeholders and concatenate with the string passed as parameters int0 the format function 
# txt3 = "My name is {}, I'm a {}".format("inie", "software engineer")
# print(txt3)

#3 Formatting String using f-strings a.k.a Literal String Interpolation
# name = "ini-ubong"
# print(f"My name is {name}.")

# exercise
backend = "I am a backend developer"
name = "My name is Inie"
# print(name + ' ' + backend)
# using "in"
# print("n" in school)
# print(school * 2)
# print(len(backend))
# print(backend[36:])

# Using string formatting (%)
# fullstack = "%s, %s %s so...just call me a software engineer:)" %(name, backend, "and also a frontend developer")
# print(fullstack)

# Using format() method
# class_d = "welcome to {} and I am {} I'm {}m tall".format("class D", name, 1.75)
# print(class_d)

# Using f-string method 
# introduction = f"Hi {name} {backend}"
# print(introduction)

# Built-in String Methods
# print(name.upper())
# new_name = name.capitalize()
# print(new_name)
# print(name.isdigit())
# print(name.endswith("Inie"))
# strip method removes the white spaces before and after a string 
# msg = "  the message  "
# print(msg.strip())

# Accessing Values in List
# list1 = ['physics','chemistry', 1997, 2000]
# list2 = [1, 2, 3, 4, 5, 6, 7]
# print(list1[0])
# print(list2[2:5])

# Updating a list
# To remove a list element, you can use the del statement(if you the exact position of the element) or use the remove() method
# list1[0] = 'biology'
# print(list1)
# print(len(list1))

# Delete List item
# del list1[2]
# print(list1)

# Basic List Operations 
# length - len()
# num = [1, 2, 3]
# numx = [4, 5, 6]
# print(len(num))

# Concatenation "+"
# print(num + numx)

# Membership
# print(3 in num)

# Iteration
# for x in numx: print(x)

# Repetion
# greeting = ['holla']
# print(greeting * 4)

# Indexing, Slicing and Matrices
# About = ['age', 'height', 'occupation'] 
# print(About[-2])
# print(About[1:])

# List built-in Methods
# append(): Adds an element at the end of the list
# insert(): Adds ''    ''    ''  a specified location
# clear(): Clears all items from the list
# sort(): To arrange all items in an orderly manner
# pop(): Removes and returns the last object or obj from the list
# remove(): Removes object from the list 
# reverse(): Reverses objects from the list in place

# people = [['maria', 21, ['frontend', "agile"]], ['john', 20, ['backend', 'frontend', 'product design']], 'sandra']
# print(people[1][2][2])
# print(10 == 9)
