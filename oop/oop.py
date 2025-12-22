"Object-oriented programming, also known as OOP, is a programming style in which developers treat everything in their code like a real-world object."

"A class is like a blueprint for creating objects. Every single object created from a class has attributes that define data and methods that define the behaviors of the objects."

# CLASS REVISION
# BASIC SYNTAX OF A CLASS
class ClassName:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sample_method(self):
        print(self.name.upper())

# NB: Attributes are like variables within a class, and are used to store data. Methods are functions defined within a class, and are the actions objects created with a class can perform.


class Dog:
    def __init__(self, dog_name, dog_age):
        self.name = dog_name
        self.dog_age = dog_age

    def bark(self):
        print(f"{self.name.capitalize()} says woof woof! I'm {self.dog_age} years old!" )

dog_one = Dog("lady", 3)
dog_two = Dog("tramp", 5)

dog_one.bark()
dog_two.bark()


# METHODS AND ATTRIBUTES
"Attributes are variables that belong to an object"

# TYPES OF ATTRIBUTES
"1. Instance Attribute" # unique to each object created from a class, and you usually set them with the __init__ method.
"2. Class Attribute" # Class attributes, belong to the class itself and are shared by all instances of that class.

"E.g"
class Bike:
    classification = "Sports" # Class Attribute

    def __init__(self, name):
        self.name = name # Instance Attribute

    def revvvv(self):
        return f"{self.name} is revvving: Vrooooom! Vrooom!!"

print("BIKE_CLASSIFICATION>>>>>>>", Bike.classification)

bike_one = Bike("Ducati")
print(bike_one.name) 
print(bike_one.classification)

bike_two = Bike("Kawasaki")
print(bike_two.name) 
print(bike_two.classification)
print(bike_two.revvvv())

"NB: You can access class attributes directly from the class itself, but you need to create an object and pass it data first before you can access instance attributes."

class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

car_one = Car("red", "Toyota Corolla")
car_two = Car("blue", "Mazda 3")


# SPECIAL METHODS | DUNDER METHODS
"Think of special methods as the directors of the activities between a person programming and the Python language interpreter itself."

# DEFINING DUNDER | SPECIAL METHODS
"E.g 1"
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages
    
    def __str__(self):
        return f"'{self.title}' has {self.pages} pages"
    
    def __eq__(self, other):
        return self.pages == other.pages
    
book_one = Book("Built Wealth Like a Boss", 420)
book_two = Book("Be Your Own Start", 420)

print(len(book_one))
print(len(book_two))
print(str(book_one))
print(str(book_two))
print(book_one == book_two)


"E.g 2 - Shopping Cart"
class Cart:
    def __init__(self, item, quantity):
        self.items = []

    def add(self, item):
        return self.items.append(item)
    
    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f"{item} is not in cart!")            
    
    def list_items(self):
        return self.items
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __contains__(self, item):
        return item in self.items
    
    def __iter__(self):
        return iter(self.items)
    



# SYNTAX
class ClassName:
    def __init__(self, parameters):
        # attribute = value
        pass

    def method_name(self):
        # method logic
        pass
