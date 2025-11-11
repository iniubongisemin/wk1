# sets are used to store multiple items in a single variable 
# they are unordered, unchangeable*, do not allow duplicates, are unindexed and written with curly brackets
# e.g creating a set
thisSet = { 'apple', 'banana', 'cherry' }
# print(thisSet)

# NB: once created, you cannot change its items, but you can remove items and add new items!   
# duplicates are not allowed, if present, they will be ignored
# e.g 
thisSet = { 'apple', 'banana', 'cherry', 'apple' }
# print(thisSet)

# the values True and 1 are considered the same value in sets, and they are treated as duplicates 
thisSet = { 'apple', 'banana', 'cherry', True, 1, 2 }
# print(thisSet)

# the False and 0 are considered the same value in sets, and are treated as duplicates
thisSet = { 'apple', 'banana', 'cherry', False, True, 0, 1 }
# print(thisSet)

# getting the length of a set
# to determine how many items a set has, use the len() function 
print(len(thisSet))

# NB: set items can be of any data type
# e.g
set1 = { 'apple', 'banana', 'cherry' }
set2 = { 1, 5, 7, 9, 3 }
set3 = { True, False, True }

# print(set1, set2, set3)

# NB: a set can contain different data types
setX = { 'abc', 34, True, 40, 'male' }
# print(setX)

# NB: in python, sets are defined as objects with the data type "set"
# print(type(setX))

# NB: you can use the set constructor to make a set
thisSet = set(('apple', 'banana', 'cherry')) # take note of the double round-brackets
# print(thisSet)

# accessing set items 
# NB: you cannot access items in a set by referring to an index or a key
# but you can loop through the set items using a "for loop", or ask if a specified value is present in a set by using the "in" keyword
# e.g loop through the set and print the values
for x in thisSet:
    pass
    print(x)

# e.g function to check if "banana" is present in the set;
# print('banana' in thisSet)

# changing items: once a set is created, you cannot change its items but you can add new items 
# use the "add()" method 
# e.g
thisSet.add('orange')
# print(thisSet) 

# adding sets: to add items from another set into the current set, use the update() method
# e.g add elements from tropical to newSet
tropical = { 'pineapple', 'mango', 'pawpaw' }
newSet = { 'apple', 'banana', 'cherry' }
newSet.update(tropical)
# print(newSet)

# adding iterables: the object in the update method does not have to be a set, it can be any iterable object(tuples, lists, dictionaries e.t.c)
# e.g adding elements of a list to a set 
thisSet = { 'apple', 'banana', 'cherry' }
myList = [ 'kiwi', 'orange' ]
thisSet.update(myList)
# print(thisSet)

# removing set items: you can use the remove() or the discard() method 
# e.g remove banana by using the remove() method
thisSet.remove('banana')
# print(thisSet)                                        

# NB: if the item to be removed does not exist, remove() will throw an error
thisSet = { 'apple', 'banana', 'cherry', False, True, 0, 1 }
thisSet.remove(1)
# print(thisSet)                                        

# discard method
thisSet.discard('mango')
# print(thisSet)                                        
# conversely, if the specified item does not exist in the set, the discard() method will NOT throw an error

# the pop() method removes a random value and the return value of this method is the removed item
# the return value of the pop() method is the removed item 
# e.g remove a random item by using the pop() method
thisSet = { 'apple', 'banana', 'cherry' }
x = thisSet.pop()
# print(x)
# print(thisSet)

# looping through set items
# you can loop through the set items by using a for loop
thatSet = { 'naruto', 'sasuke', 'sakura' }
for x in thatSet:
    pass
    # print(x)

# joining two sets
# there are several methods, you can use the union() method: it returns a new set containing all items from both sets or;
# e.g union() method returns a new set containing all items from both sets
alphabet = { 'a', 'b', 'c' }
numeral = { 1, 2, 3 }
alphaNumeric =  alphabet.union(numeral)
# print(alphaNumeric)

numericAlpha = numeral.union(alphabet)
# print(numericAlpha) # NB: because sets do not have an indexing order, it doesn't matter what format you use to join the different sets

# the update() method inserts all the items from one set into another
# e.g 
alphabet.update(numeral)
# print(alphabet)
# PS: both union() and update() will exclude any duplicate items

# HOW TO keep ONLY the duplicates: 
# use the intersection_update() method to keep only the items that are present in both sets 
# e.g keep the items that exist in both set x and set y
x = { 'apple', 'banana', 'cherry' }
y = { 'google', 'microsoft', 'apple' }
x.intersection_update(y)
# print(x)

# the intersection() method returns a new set that only contains the items that are present in both sets
# e.g return a set that contains the items that exist in both set x and set y
x.intersection(y)
# print(x)

# how to keep all EXCEPT the duplicates 
# the symmetric_difference_update() method updates the SET CALLING THE METHOD with elements that are in either of the sets, but not common to both
# PS: the original set is modified in-place
# e.g keep the items that are not present in both sets
x = { 'apple', 'banana', 'cherry' }
y = { 'google', 'microsoft', 'apple' } 
x.symmetric_difference_update(y)
print(x)

# the symmetric_difference() method returns a new set containing elements that are in either of the sets but not common to both;
# PS: the original sets remain unchanged!
# e.g returns a NEW SET containing all the items from both sets, EXCEPT items that are present in both 
x = { 'apple', 'banana', 'cherry' }
y = { 'google', 'microsoft', 'apple' }
z = x.symmetric_difference(y)
print(z)

# using python sets to manage unique user IDs in a database
user_ids = { 101, 102, 103, 104 }
new_user_id = 105

# check if a user ID exists
if new_user_id in user_ids:
    print(f"user ID {new_user_id} already exists")
else:
    user_ids.add(new_user_id)
    print(f"user ID {new_user_id} added successfully")

# NB: in sets, True == 1; False == 1

# set methods 
# METHOD                               DESCRIPTION
# add()                                adds an element to the set
# clear()                              removes all the elements from the set 
# copy()                               returns a copy of the set 
# difference()                         returns a set containing the difference between two or more sets
# difference update()                  removes the items in this set are also included in another specified set 
# discard()                            removes the specified item()
# intersection()                       returns a set that is the intersection of two or more sets
# intersection update()                removes the items in this set that are not present in other specified set(s)
# isdisjoint()                         returns whether two sets have an intersection or not 
# issubset()                           returns whether another set contains this set or not
# issuperset()                         returns whether this set contains another set or not
# pop()                                removes an element from the set
# remove()                             removes the specified element
# symmetric difference()               returns a set with the symmetric differences of two sets
# symmetric difference update()        inserts the symmetric differences from this set and another 
# union()                              returns a set containing the union of sets
# update()                             updates the set with another set or any other iterable 