# lists: they're used to store multiple items in a single variable 
# create a list
thisList = [ 'apple', 'banana', 'cherry' ]
# print(thisList)

# NB: list items are indexed, ordered, changeable, and allow duplicate values

# list length
# print(len(thisList))

# list items - data types 
# list items can be of any data type
list1 = [ 'apple', 'banana', 'cherry' ]
list2 = [ 1, 3, 44, 6, 90 ]
list3 = [ True, False, True ]

# print(list3)

# the list() constructor
# it is possible to use the list constructor when creating a new list
newList = list(('pineapple', 'avocado', 'grape')) # take note of the double round brackets!
# print(newList)

myName = ['iniubong', 'isemin', 'enyinna']
# print(myName[0])

# range of indices
cars = ['ferrari', 'mustang', 'porshe', 'lamborghini', 'bugatti', 'viper']
# print(cars[2:4])

# print(cars[:4])
# print(cars[4:])
# print(cars[4:5])

# range of negative indices 
# print(cars[-4:-1])

# check if item exists using the "in" keyword
if 'bugatti' in cars:
    pass
    # print('yo! i\'m bugatti in your fleet of cars boss')

fruits = ['apple', 'pineapple', 'banana', 'orange', 'avocado', 'coconut']
fruits[3] = 'strawberry'
# print(fruits)

# changing a range of item values
# to change the value of items within a specific range, define a list with the new values and refer to the range of index numbers where you want to insert the new values
fruits[2:5] = ['tigernut', 'lemon', 'grapes']
# print(fruits)

fruits[1:3] = ['breadfruit']
# print(fruits)

# insert items 
# to insert a new list item without replacing any of the existing values, we can use the "insert()" method
# the "insert()" method inserts an item at the specified index
fruits.insert(2, 'dates')
# print(fruits)

# append items
# to add items to the end of the list, use the append() method
# e.g 
fruits.append('aubergine')
# print(fruits)

# extend list
# to append elements from another list to the current list, use the "extend()"
suv = ['cybertruck', 'jeep', 'range-rover']
suv.extend(cars)
# print(suv)

# adding iterables and collections
# NB: the extend method doesn't only append lists, you can add tuples, sets, dictionaries etc.
suvTuple = ('tundra', 'tacoma', 'edge', 'explorer')
suv.extend(suvTuple)
# print(suv)

# add list items 
# append items: to add items to the list, use the append() method;
thisList = [ 'apple', 'banana', 'cherry' ]
thisList.append('orange')
# print(thisList)

# insert items: to insert an item at a specified index => insert() method
thisList.insert(1, 'pineapple')
# print(thisList)

# extend list: used to append elements from another list
citrusFruits = [ 'lemon', 'tangerine', 'grape' ]
# thisList.extend(citrusFruits)
thisList.append(citrusFruits)
# print(thisList)

# NB: you can use the extend method to append any iterable object 
# e.g 
citrus = ('lemon', 'tangerine', 'grape')
# thisList.append(citrus)
thisList.extend(citrus)
# print(thisList)

# removing list items 
# remove() method removes the specified item(s)
fruits = ['apple', 'pineapple', 'banana', 'cherry', 'orange', 'lemon', 'tangerine', 'grape']
fruits.remove('apple')
# print(fruits)

# NB: if there is more than one item with the specified value, the remove() method only removes the first occurence 
numbers = [ 1, 3, 4, 5, 7, 8, 3, 0, 3 ]
# print(numbers)
numbers.remove(3)
# print(numbers)

# removing specified index
# pop() method removes the specified index
numbers.pop(2)
# print(numbers)

# NB: if you do not specify the index, the pop() method removes the last item
numbers.pop()
# print(numbers)

# the del keyword also removes the specified index 
del numbers[4]
# print(numbers)

# the del keyword can also be used to delete the entire list 
# del numbers
# print(numbers)

# clearing the list
# the clear() method empties the list, the list remains but it has no items in it
numbers.clear()
# print(numbers)

# looping through a list 
# for loops
# e.g print all the items i the list, one by one
num = [ 1, 3, 4, 5, 8, 3, 9, 3 ]
for x in num:
    pass
    # print(x)

# looping through the index numbers 
# you can also loop through the list items by referring to their index number 
# use the range() and len() functions to create a suitable iterable 
for x in num: 
    pass
    # range(len(num))
    # print(num[i])

# while loops 
# use the len() function to determine the length of the list, then start at and loop your way through the list items by referring to their indices
# PS: remember to increase the index by one after each iteration 
# e.g print all items, using a while loop to go through all the index numbers 
i = 0
while i < len(num):
    pass
    # print(num[i])
    i = i + 1

# list comprehension  
# it offers the shortest sytax for looping through a list
# e.g a shorthand that will print all items that will 
# [print(x) for x in num]               

# e.g based on a list of fruits, you want new lists, containing only the fruits with the letter "a" in the name 
# NB: without list comprehension, you will have to write a "for" statement with a conditional test inside 
fruitList = [ 'apple', 'banana', 'cherry', 'kiwi', 'mango' ]
newList = []

for x in fruitList:
    if "a" in x:
        newList.append(x)

# print(newList)

# NB: with list comprehension, you can do all that with one line of code
newList = [x for x in fruitList if "a" in x]
# print(newList)

# syntax:
# newList = [expression "for" item "in" iterable "if" condition == true]
# NB: the return value is a new list, leaving the old list unchanged 
# NB: the condition is like a filter that only accepts the items that valuate to "True"

# list comprehension to only accept items that are not "apple"
newList = [ x for x in fruitList if x != "apple" ]
# print(newList)

# iterable
# it is essentially any object that you can carry out iteration action upon e.g list, tuple, set, dictionary, string etc.

# e.g using the range to create an iterable 
iterable = [ x for x in range(10) ]
# print( iterable )

# iterable to accept only numbers < 5 in a range
iterable = [ x for x in range(10) if x < 5 ]
# print(iterable)

# expression 
# it is the "current item" in the iteration, but it is also the "outcome", which you can "manipulate" before it ends up like a list in the new list 
# e.g set the values in the new listt to upper case;
newList = [ x.upper() for x in fruitList ]
# print(newList)

# e.g set all the values in the new list to "hello"
newList = ['hello' for x in fruitList]
# print(newList)

# NB: the expression can also contain conditions, not like a filter, but as a wau to maniputlate the outcome;
# e.g program to return an item if it is not x, if it is x, it should return y
newList = [ x if x != "banana" else "orange" for x in fruitList]
# print(newList)

# sort lists
# list objects have a sort() method that will sort the list alphanumerically, 
thisList = [ 'orange', 'mango', 'kiwi', 'pineapple', 'banana' ]
thisList.sort()
# print(thisList)

thisList.sort(reverse = True)
# print(thisList)

# sorting a list numerically 
thisList = [100, 50, 65, 82, 23]
thisList.sort()
# print(thisList)

# sort descending
# to sort descending, use the keyword argument "reverse = True"
# e.g 
thisList.sort(reverse = True)
# print(thisList)

# customize sort function
# you can also customize your function by using the keyword argument "key = function"
# the function will return a number that will be used to sort the list (the lowest number first)
# e.g sort the list based on how close the number is to 50
def myfunc(n):
    return abs(n - 50)

thisList = [100, 50, 65, 82, 23]
thisList.sort(key = myfunc)
# print(thisList)
   
# case insensitive sort 
# by default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters 
# case sensititve sortiing can give an unexpected result; 
# # e.g
thisList = [ 'banana', 'Orange', 'Kiwi', 'cherry' ]
thisList.sort()
# print(thisList)

# you can use built-in functions as key functions when sorting a list 
# for case-insensitive sorting, use str.lower as a key function 
# e.g to perform case insensitive sorting;
thisList = [ 'banana', 'Orange', 'Kiwi', 'cherry' ]
thisList.sort(key = str.lower)
# print(thisList)

# reversing the order of a list regardless of the alphabet 
# "reverse()" method reverses the current sorting order of the elements
# e.g
thisList = [ 'banana', 'Orange', 'Kiwi', 'cherry' ]
thisList.reverse()
# print(thisList)

# copying lists in python 
# you can't copy a list by simply typing list1 = list2 because list2 will only be a reference to list1 & changes made in list1 will also be made in list2
# you can copy a list by using the built-in list method "copy()"
thisList = [ 'apple', 'banana', 'cherry' ]
myList = thisList.copy()
# print(myList)

# you can also use the built-in "list()" method
myList = list(thisList)
# print(myList)

# joining two lists 
# you can use the "+" operator
# e.g
list1 = [ 'a', 'b', 'c' ]
list2 = [ 1, 2, 3 ]
list3 = list2 + list1
# print(list3)

# we can join two lists by appending the items from list2 into list1 one by one
# list3 = list1.append(list2) ...this will return "None", use a function!
# for x in list2:
#     list1.append(x)

# print(list1)

# for x in list1:
#     list2.append(x)

# print(list2)

# you can also use the extend method, where the purpose is to add elements fromm one list to another list
list1.extend(list2)
print(list1)

# python list methods index
# method     description 
# append()   adds an element at the end of the list
# clear()    removes all the elements from the list
# copy()     returns a copy of the list 
# count()    returns the number of elements in the specified value
# extend()   adds the elements of a list (or any iterable), to the end of the current list
# index()    returns the index of the first element with the specified value
# insert()   reverses the order of the list 
# sort(cfctc)     sorts the list        

