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
    def __init__(self):
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
    
cart = Cart()
cart.add("HP Laptop")
cart.add("Logitech Wireless Mouse")
cart.add("Ergo Keyboard")
cart.add("Monitor")

for item in cart:
    print(item, end='\n')

print("No of items in cart: ", len(cart))
print(cart[3])
print("Monitor" in cart )
print("Wireless earphones" in cart)

cart.remove("Ergo Keyboard")

print(cart.list_items())

cart.remove("Wireless earphones")


# HANDLING OBJECT ATTRIBUTES DYNAMICALLY
"1. getattr()" # For Reading an attribute from an object at runtime
"2. setattr()" # For Creating new OR Updating an existing attribute
"3. hasattr()" # For Verifying whether or not an attribute EXISTS before using it or deleting it
"4. delattr()" # For removing an attribute dynamically

"NB: You can access, modify, check, or even delete attributes using their names as variables and not as fixed names in your code"


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Lamborghini", "Gallardo")
print(my_car.brand)
print(my_car.model)

# SYNTAX
"1. getattr(object, attribute_name, default_value)"

"E.g"
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("John Doe", 28)

print(getattr(person, "name"))
print(getattr(person, "age"))
print(getattr(person, "city", "Lagos")) # NB: Lagos is a default

"NB: When the attribute name comes from a variable, i.e from user input or say a file, you CAN'T user 'object.attribute_name' syntax"

attr_name = input("Enter the attribute name you want to see: ")
print(getattr(person, attr_name, "Attribute not found!"))


# HOW TO CHECK IF AN ATTRIBUTE IS PRESENT IN A CLASS USING A CUSTOM METHOD

for attr in dir(person):
    if not attr.startswith('__') and not callable(getattr(person, attr)):
        value = getattr(person, attr) 
        print(f"{attr}: {value}")

# SYNTAX
"2. setattr(object, attribute_name, value)"

"E.g"
class Configuration:
    pass

settings_data = {
    "server_url": "https://api.example.com",
    "timeout_sec": 30,
    "max_retries": 5
}

config_obj = Configuration()

for attr_name, attr_value in settings_data.items():
    setattr(config_obj, attr_name, attr_value)

print(config_obj.server_url)
print(config_obj.timeout_sec)
print(config_obj.max_retries)

# SYNTAX
"3. hasattr(object, attribute_name)"

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

product_a = Product("T-Shirt", 25)

required_attributes = ["name", "price", "inventory_id"]

for attr in required_attributes:
    if not hasattr(product_a, attr):
        print(f"ERROR: Product is missing the required attribute: '{attr}'")
    else:
        print(f"{attr}: {getattr(product_a, attr)}")

# SYNTAX
"4. delattr(object, attribute_name)"

"E.g: Cleaning up sensitive info from a user session"
class UserSession:
    def __init__(self, user_id, token):
        self.user_id = user_id
        self.auth_token = token # sensitive
        self.temp_counter = 0

session = UserSession(101, "a1b2c3d4e5")

attributes_to_clean = ["auth_token", "temp_counter"]

for attr in attributes_to_clean:
    if hasattr(session, attr):
        delattr(session, attr)
        print(f"Removed attribute successfully: {attr}")
    
print("\nFinal attributes remaining: ")

for attr in dir(session):
    if not attr.startswith("__") and not callable(getattr(session, attr)):
        print(f" - {attr}: {getattr(session, attr)}")