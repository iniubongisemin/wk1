"Object-oriented programming, also known as OOP, is a programming style in which developers treat everything in their code like a real-world object."

# SYNTAX
class ClassName:
    def __init__(self, parameters):
        # attribute = value
        pass

    def method_name(self):
        # method logic
        pass


class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car_one = Car("Lamborghini", "black")
car_two = Car("Ferrari", "red")

print("Car One  Brand", car_one.brand)
print("Car One  Color", car_one.color)
print("Car Two  Brand", car_two.brand)
print("Car Two  Color", car_two.color)

"OOP has four paradigms/principles that help you organize & manage code effectively:"
"1. Encapsulation"
"2. Inheritance"
"3. Polymorphism"
"4. Abstraction"

# OOP >> EIPA

"#1. ENCAPSULATION"
"Encapsulation is the bundling of the attributes and methods of an object into a single unit -- the class."

"""
Let's say you want to track a wallet balance. You want to allow people to deposit or withdraw money from the wallet, but no one should be able to tamper with the balance directly.
In that case, you can make deposit() and withdraw() public methods, and you hide the balance under the _balance attribute:
"""

class Wallet:
    def __init__(self, balance):
        self._balance = balance # For internal use by convention

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount # Add to the balance safely

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount # Remove from the balance safely

"NB: By convention, prefixing attribute and methods with a single underscore means they are meant for internal use"

class Wallet:
    def __init__(self, balance):
        self.__balance = balance # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount # Add to the balance safely

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount # Remove from the balance safely

account = Wallet(500)
# print(account.__balance) # AttributeError: 'Wallet' object has no attribute '__balance'

"NB: To get the balance, we add a get balance method"

class Wallet:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance
    
account = Wallet(500)
print(f"Here's your account balance ₦{account.get_balance()}")

account.deposit(100000)
print(f"Here's your account balance ₦{account.get_balance()}")

account.withdraw(25000)
print(f"Here's your account balance ₦{account.get_balance()}")

# You can also define a private __validate method to check if every deposit or withdrawal amount is a positive number:
class Account:
    def __init__(self):
        self.__balance = 0

    def __validate(self, amount):
        if amount < 0:
            raise ValueError("Amount MUST be positive")
        
    def deposit(self, amount):
        self.__validate(amount)
        self.__balance += amount

    def withdraw(self, amount):
        self.__validate(amount)
        if amount > self.__balance:
            raise ValueError("Insufficient Funds")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

my_account = Account()
my_account.deposit(10000000)
print(f"Here's your account balance ₦{my_account.get_balance()}")
my_account.withdraw(5000000)
        
"GETTERS & SETTERS"
"Getters and setters are methods that let you control how the attributes of a class are accessed and modified."

"These actions are done through what's known as properties. They are what connect getters and setters, and allow access to data."

"Properties act like attributes but behave like methods under the hood." 
"PPS: You can access properties with dot notation instead of parentheses or round brackets -- Their main purpose is readability!"

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self): # A getter to get the radius
        return self._radius
    
    @property
    def area(self): # A getter to calculate area
        return 3.14 * (self._radius ** 2)
    
my_circle = Circle(3)
print("RADIUS>>>>", my_circle.radius)
print("AREA>>>>", my_circle.area)

"USING PROPERTIES TO SET ATTRIBUTES"
"SYNTAX: @<property_name>.setter"

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self): # A getter to get the radius
        return self._radius
    
    @radius.setter
    def radius(self, value): # A setter to set the radius
        if value <= 0:
            raise ValueError("Radius MUST be positive!")
        self._radius = value

gold_circle = Circle(3)
print("INITIAL RADIUS>>> ", gold_circle.radius) 

gold_circle.radius = 8
print("MODIFIED RADIUS>>> ", gold_circle.radius) 

"NB: Once you define getters and setters, Python automatically calls them under the hood whenever you use normal attribute syntax:"
"E.g"
print("INITIAL RADIUS>>> ", gold_circle.radius) # This will call the getter
gold_circle.radius = 10 # This will call the setter

print("NEW RADIUS>>> ", gold_circle.radius) 

"NB: Note that inside the setter, you cannot use same name of the property when assigning a new value."

"DELETER"
"A deleter runs custom logic when you use the del statement on a property."

"SYNTAX: @<property_name>.deleter:"

class Circle:
    def __init__(self, radius):
        self._radius = radius

    # GETTER
    @property
    def radius(self):
        return self._radius
    
    # SETTER
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius MUST be positive!")
        self._radius = value

    # DELETER
    @radius.deleter
    def radius(self):
        print("Deleting radius....")
        del self._radius
        print("Radius deleted!")

# How to Delete it
# Create the Instance
my_circle = Circle(33)
print("Initial radius: ", my_circle.radius)

# Delete the radius
del my_circle.radius

# Confirm Deletion
try:
    print(my_circle.radius)
except AttributeError as e:
    print("Error", str(e))



"#2. INHERITANCE"
"With inheritance, a subclass (or child class) can use the attributes and methods of a base class (or parent class). This allows you to reuse code, create clear class hierarchies, and customize behavior without rewriting everything."

# SYNTAX
class Parent:
    # Parent atttibutes & Methods
    pass

class Child(Parent):
    # Child inherits, extends and/or overrides where necessary
    pass

"NB: For the Child class to inherit from the Parent class, you have to pass the Parent to the Child." 
# - SINGLE INHERITANCE i.e The child class inherits from exactly one parent class

"E.g"
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f"{self.name} makes a sound"
    

class Dog(Animal):
    bark = "woof! woof!! woof!!!"

jack = Dog("Jack")
# print(jack.sound()) 
# print(jack.bark)

"OVERRIDING THE SOUND METHOD"
    
class Dog(Animal):
    bark = "Woof! Woof!! Woof!!!"

    def sound(self):
        return f"{self.name} barks {self.bark}"
    
scott = Dog("Scott")
# print(scott.sound())

"NB: You can keep the return value of sound() and add the bark class variable later, you can extend sound() by using the super() function"
class Dog(Animal):
    bark = "Woof! Woof!! Woof!!!"

    def sound(self):
        dunder = super().sound()
        return f"{dunder}, then {self.name} barks {self.bark}"

tramp = Dog("Tramp")
print(tramp.sound())