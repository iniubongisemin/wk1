# dictionaries are used to store data values in key:value pairs
# they are ordered, changeable and do not allow duplicates!
# e.g of a dictionary
thisDict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
# print(thisDict)

# DICTIONARY ITEMS
# they are presented in key:value pairs and can be referred to by using the key name
# print the 'brand' value of the dictionary
# print(thisDict['brand'])

# NB: duplicate values will overwrite existing values 
thisDict = {
    'brand': 'Ford', 
    'model': 'Mustang',
    'year': 1964,
    'year': 2020
}
print(thisDict)

# DICTIONARY LENGTH
# use the len() function to determine the number of items a dictionary has 
print(len(thisDict))

# DICTIONARY ITEMS - DATA TYPES
# the items in a dictionary can be of any data type!
# e.g string, int, boolean and list data types
mixDict = {
    'brand': 'Ford',
    'electric': False,
    'models': [ 'Mustang', 'Taurus' ],
    'year': 1964,
    'colors': [ 'red', 'white', 'blue' ]
}
print(mixDict)

# type(): in python, dictionaries are defined as objects with the data type 'dict'
print(type(thisDict))

# the dict() constructor
# you can use the dict() method to make a dictionary
newDict = dict(name = 'inie', age = '2x', country = 'nigeria')
print(newDict)

# ACCESSING DICTIONARY ITEMS 
# you can access dictionary items by referring to its key name, inside square brackets;
# e.g get the value of the 'model' key:
x = mixDict['models']
print(x)

# NB: the "get()" method will also give you the same result
y = mixDict.get('models')
print(y)

# GETTING KEYS: the "keys()" method will return a list of all the keys in the dictionary
z = mixDict.keys()
# print(z)

# PS: the list of the keys is a view of the dictionary hence, any changes made to the original dictionary will be reflected in the keys list
# e.g add a new item to the original dictionary and see that the keys list gets updated as well 
car = {
    'brand': 'Ford', 
    'model': 'Mustang', 
    'year': 1964
}
x = car.keys()
# print(x) # before the change

car['color'] = 'white'
# print(x) # after the change

# GET VALUES
# the values() method will return a list of all the values in the dictionary
# e.g get a list of the values:
x = car.values()
# print(x)

# NB: the list of the values is a view of the dictionary, i.e any changes done to the dictionary will be reflected in the values list
# e.g make a change in the original dictionary and see that the values list gets updated as well:
z = car.values()
# print(z) # before the change 

car['year'] = 2020
# print(z) # after the change 

# e.g add a new item to the original dictionary and see that the values list gets updated as well
a = car.values()
# print(a) # before the change 

car['color'] = 'red'
# print(a) # after the change

# GETTING ITEMS
# the items() method returns each item in a dictionary, as tuples in a list 
# e.g get a list of the key:value pairs
x = mixDict.items()
# print(x)

# NB: the returned list is a view of the items of the dictionary, i.e any changes done to the dictionary will be reflected in the items list
# e.g make a change in the original dictionary and observe that the items list gets updated as well 
car = {
    'brand': 'Ford', 
    'model': 'Mustang',
    'year': 19634
}
x = car.items()
# print(x) # before the change 

car['year'] = 2020
# print(x) # after the change

# e.g add a new item to the original dictionary and observe the list gets updated as well;
# print('before the change:', x) # before the change

car['decal'] = 'flames'
# print('after the change:', x) # after the change

# CHECKING IF KEY EXISTS
# to determine if a specified key is present in a dictionary, use the "in" keyword
# e.g check if "model" is present in the dicitonary
if 'model' in car:
    pass
    # print('yes, "model" is one of the keys in the car dictionary')

# CHANGING DICTIONARY ITEMS 
# CHANGING VALUES: you can change the value of a specific item by referring to its key name:
# e.g change the "year" to 2018
car['year'] = 2018
# print(car)

# UPDATING A DICTIONARY 
# the update method updates the dictionary with the items from the given argument
# PS: the argument must be a dictionary or an iterable object with key:value pairs
# e.g update the model of the car by using the "update()" method
car.update({'model': 'explorer'})
# print(car)

# ADDING DICTIONARY ITEMS
# adding an item to the dictionary is done by using a new index key and assigning a value to it 
car['tires'] = 'tubeless'
# print(car)

# REMOVING ITEMS 
# the "pop()" method removes the item with the specified key name:
# car.pop('model')
# print(car)

# the "popitem()" method removes the last inserted item 
car.popitem()
# print(car)

# the "del" keyword removes the item with the specified key name:
# del car['year']
print(car)

# PS: the del keyword can also delete the dictionary completely 
# del car
# print(car) error: name 'car' is not defined because it no longer exists

# the "clear()" method empties the dictionary
thisDict.clear()
# print(thisDict)

# LOOPING DICTIONARIES
# you can loop through a dictionary using a for loop 
# PS: when looping through a dictionary, the return values are the keys of the dictionary, but there are methods to return the values as well
# e.g print all key names in the dictionary one by one;
for x in car:
    pass
    # print(x)

# e.g print all values in the dictionary one by one
for x in car:
    pass
    # print(car[x])

# PS: you can also use the "values()" method to return the values of a dictionary 
for x in car.values():
    pass
    # print(x)

# PPS: you can also use the "keys()" method to return the keys of a dictionary 
for x in car.keys():
    print(x)

# PPPS: you can loop through both keys and values by using the items() method:
for x, y in car.items():
    print(x, y)

# COPYING DICTIONARIES
# you cannot copy a dictionary by simply typing dict2 = dict1, because dict2 will only be a reference to dict1 and changes made in dict1 will automatically also be made in dict 2
# use the "copy()" method to make a copy
# e.g make a copy of a dictionary with the copy() method;

raceCar = {
    'brand': 'Chevrolet',
    'model': 'Camarro',
    'year': 2024,
    'decals': 'flames'
}

sportsCar = raceCar.copy()
# print(sportsCar)

# PS: another way to make a copy is to use the built-in function "dict()"
# e.g make a copy of a dictionary with the dict() function;
ford = dict(car)
# print(ford)

# NESTED DICTIONARIES
# a dictionary that contains another dictionary is called nested dictionaries
# e.g create a dictionary that contains four dictionaries;
monFamille = {
    'firstChild': {
        'name': 'Uriel',
        'dob': 2026
    },
    'secondChild': {
        'name': 'Hephzibah',
        'dob': 2028
    },
    'thirdChild': {
        'name': 'Eugene',
        'dob': 2030
    },
    'fourthChild': {
        'name': 'Hadassah',
        'dob': 2032
    }
}
print(monFamille)

# alternatively, you can add three dictionaries into a new dictionary;
# e.g create three dictionaries, then create one dictionary that will contain the other thee dictionaries
firstChild = {
    'name': 'Uriel', 
    'dob': 2026
}
secondChild = {
    'name': 'Hephzibah', 
    'dob': 2028
}
thirdChild = {
    'name': 'Eugene',
    'dob': 2030
}
fourthChild = {
    'name': 'Nightingale',
    'dob': 2032
}

myFamily = {
    'firstChild': firstChild,
    'secondChild': secondChild,
    'thirdChild': thirdChild,
    'fourthChild': fourthChild
}
print(myFamily)

# ACCESSING ITEMS IN NESTED DICTIONARIES
# to access items, use the name of the dictionary, starting with the outer dictionary;
print(myFamily['secondChild']['name'])

# DICTIONARY METHODS
# python has a set of built-in methods that you can use on dictionaries
# METHOD                DESCRIPTION
# clear()               removes all the elements from the dictionary
# copy()                returns a copy of the dictionary
# fromkeys()            returns a dictionary with the specified keys and value
# get()                 returns the value of the specified key
# items()               returns a list containing a tuple for each key value pair
# keys()                returns a list containing the dictionary's keys 
# popitem()             removes the last inserted key-value pair
# setdefault()          returns the value of the specified key. if the key does not exist, insert the key with the specified value
# update()              updates the dictionary with the specified key-value pairs
# values()              returns a list of all the values in the dictionary
