# a tuple is a collection which is ordered, indexed, unchangeable and allows duplicates...they are written with round brackets ()
thisTuple = ('apple', 'banana', 'cherry')
# print(thisTuple)

thisTuple = ('apple', 'banana', 'cherry', 'apple', 'cherry')
# print(thisTuple)

# tuple length
# use len() function to determine how many items a tuple contains
# print(len(thisTuple))

# creating a tuple with only one item
# you must add a comma after the item else python won't recognise it as a tuple!
myTuple = ('first')
# print(myTuple)
# print(type(myTuple)) # NOT a tuple

thisTuple = ('first',)
# print(type(thisTuple)) # this is a tuple 

# tuple items can be of any data type
tuple1 = ('apple', 'banana', 'cherry')
# print(tuple1)
tuple2 = (1, 5, 7, 9, 3)
# print(tuple2)
tuple3 = (True, False, True)
# print(tuple3)

# tuple with different data types 
tuple1 = ('abc', 34, True, 40, 'male')
# print(tuple1)

# type(): in python, tuples are objects with the data type 'tuple'
# print(type(tuple1))

# the tuple constructor: you can use the "tuple()" to make a tuple
# e.g using the tuple() method to make a tuple 
thisTuple = tuple(('apple', 'banana', 'cherry')) # take note of the double round brackets
# print(thisTuple)

# accessing tuple items 
# this is done by referring to the index number, inside square brackets
# e.g print the second item in the tuple;
thisTuple = ('apple', 'banana', 'cherry')
# print(thisTuple[1])

# negative indexing i.e starting the index from the end 
# PS: -1 refers to the last item in the tuple
# e.g print the last item of the tuple
# print(thisTuple[-1])

# range of indices: you can specify a range of indices by specifying where to start and where to end the range 
# NB: when specifying a range, the return value will be a new tuple with the specified items 
# e.g return the third, fourth and fifth item
thisTuple = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')
# print(thisTuple[2:5]) # NB: the search will start at index 2 (included) and end at index 5 (not included)

# by leaving out the start value, the range will start at the first item
# print(thisTuple[:5])

# by leaving out the end value, the range will go on to the end of the tuple
# print(thisTuple[2:])

# range of negative indices: specify negative indices if you want to start the search from the end of the tuple;
# e.g return the items from index -4 (included) to index -1 (excluded)
# print(thisTuple[-4:-1])

# checking if an item exists: use the "in" keyword
if "apple" in thisTuple:
    pass
    # print('yes, "apple" is in the fruits tuple')

# updating tuples 
# NB: tuples are unchangeable, meaning that you cannot change, add or remove items once the tuple is created...but there are some workarounds e.g;
# how to "change" tuple values: this can be done by converting the tuple to a list and then converting the list back to a tuple 
x = ('apple', 'banana', 'cherry')
y = list(x)
y[1] = 'kiwi'
x = tuple(y)
# print(x)

# "adding" items to a tuple
# NB: since tuples are immmutable, they do not have a built-in append() method, but there are other ways to add items to a tuple e.g
#1. convert it to a list: jsut like the previous example
#2. add a tuple to a tuple 
# e.g using the list conversion method;
thisTuple = ('apple', 'banana', 'cherry')
y = list(thisTuple)
y.append('orange')
thisTuple = tuple(y)
# print(thisTuple)

# e.g darling the tuple addition method
z = ('orange',)
# newTuple = thisTuple + z
# print(newTuple) 

# alternatively using the augmented assignment operator;
thisTuple += z
# print(thisTuple)

# "removing" items from a tuple
# NB: you cannot "remove" items from a tuple! but you can use the workarounds above
# thisTuple -= z       # NB: this operation is not allowed as tuples are immutable
# print(thisTuple)

newList = list(thisTuple)
# print(newList)

newList.pop()
# print(newList)

thisTuple = tuple(newList)
# print(thisTuple)

newList = list(thisTuple)
newList.remove('cherry')
# print(newList)

thisTuple = tuple(newList)
# print(thisTuple)

# you can also use del to delete the tuple
del thisTuple
# print(thisTuple)
# it will throw an error: NameError: name 'thisTuple' is not defined

# unpacking tuples
# when you create a tuple, you normally assign values to it...this is a.k.a "packing" a tuple
# e.g
fruits = ('apple', 'banana', 'cherry')
# NB: you can also extract the values back into variables...this is a.k.a "unpacking"

# e.g 
(green, yellow, red) = fruits
# print(green)
# print(yellow)
# print(red)

# NB: the number of variables must match the number of values in the tuple, else you must use an asterisk to collect the remaining values as a list
berries = ('strawberry', 'raspberry', 'gooseberry', 'mulberry', 'burberry')
(blue, red, *List) = berries
# print(blue)
# print(red)
print(List)

# NB: if the asterisk is added to another variable name other than the last, python will assign values to the variable until the number of values left matches the number of variables left
fruits = ('apple', 'mango', 'papaya', 'pineapple', 'cherry')
(green, *tropic, orange) = fruits
# print(green)
# print(tropic)
# print(orange)

# looping through tuples 
# you can loop through the tuple items by using a for loop
# e.g iterate through the items and print the values
thisTuple = ('apple', 'banana', 'cherry')
for x in thisTuple:
    pass
    # print(x) 

# looping through the index numbers: you can also loop through the tuple items by referring to their index numbers
# use the "range()" and "len()" functions to create a suitable iterable
thisTuple = ('apple', 'banana', 'cherry')
for i in range(len(thisTuple)):
    pass
    # print(thisTuple[i])

# using a while loop: you can also loop through the tuple items by using a while loop 
# use the "len()" function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by referring to their indices 
# NB: remember to increase the index by 1 after each iteration
# e.g print all items using a "while loop" to go through all the index numbers;
thisTuple = ('raspberry', 'gooseberry', 'mulberry')
i = 0
while i < len(thisTuple):
    # print(thisTuple[i])
    i += 1

# joining tuples: you can join two or more tuples you can use the "+" operator
tuple1 = ('a', 'b', 'c')
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
# print(tuple3)

# multiplying tuples: to multiply the content of a tuple a given number of times, you can use the "*" operator
# e.g
fruits = ('apple', 'banana', 'cherry')
myTuple = fruits * 2
print(myTuple)

# tuple methods: there are two built-in methods that you can use on tuples
# method        description 
# count()       returns the number of times a specified value occurs in a tuple
# index()       searches the tuple for a specified value and returns the position of where it was found

# tuple count() method
# syntax: tuple.count(value)
# parameter values 
# parameter     description
# value         required. the item to search for 
# e.g return the number of times the value 5 appears in the tuple 
thisTuple = (1, 3, 7, 8, 5, 4, 6, 8, 5)
x = thisTuple.count(5)
print(x)

# tuple index() method
x = thisTuple.index(5)
print(x)
# definition and usage
# it finds the first occurence of the specified value 
# it raises an exception if the value is not found
# tuple.index(value)
# parameter values
# parameter     description
# value         required. the item to search for

