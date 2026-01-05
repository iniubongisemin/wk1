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
        base = super().sound()
        return f"{base}, then {self.name} barks {self.bark}"

tramp = Dog("Tramp")
print(tramp.sound())

"NB:  base is the result of calling the sound() method from the Animal class"

"MULTIPLE INHERITANCE"
# SYNTAX
class Parent:
    # Attributes and methods for Parent
    pass

class Child:
    # Attributes and methods for Child
    pass

class GrandChild(Parent, Child):
    # GrandChild inherits from both Parent and Child
    # GrandChild can combine or override behavior from each
    pass

"E.g"
class Walker:
    def walk(self):
        return "I can walk on land"
    
class Swimmer:
    def swim(self):
        return "I can swim in water"
    
class Amphibian(Walker, Swimmer):
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"I'm {self.name} the frog. {self.walk()} and also, {self.swim()}."
    
frog = Amphibian("Freddy")
print(frog.introduce())


"#3. POLYMORPHISM"
"Polymorphism allows methods in different classes to share the same name but perform different tasks. You call the same method name on different objects, and each responds in its own way."

# SYNTAX
class A:
    def action(self): ...

class B:
    def action(self): ...

class C:
    def action(self): ...

"Class().method()" # Works for A, B, or C

"E.g"
class Cat:
    def speak(self):
        return "A cat meows"
    
class Bird:
    def speak(self):
        return "A bird tweets"
    
class Monkey:
    def speak(self):
        return "A monkey ooh oooh ooh aah ooh ooh ooh aah"
    
def animal_sound(animal):
    print(animal.speak())

animal_sound(Cat())
animal_sound(Bird())
animal_sound(Monkey())

"E.g 2"
class Twitter:
    def __init__(self, content):
        self.content = content

    def post(self):
        return f"🐦 Tweet: '{self.content}' (280 chars max)"
    
class Instagram:
    def __init__(self, content):
        self.content = content

    def post(self):
        return f"📸 Instagram Post: '{self.content}' + ✨ filters"
    
class LinkedIn:
    def __init__(self, content):
        self.content = content

    def post(self):
        return f"💼 LinkedIn Article: '{self.content}' (Professional Mode)"
    
def start(social_media):
    print(social_media.post()) # Calls .post() on any object

# Instances
tweet = Twitter("Revising Python polymorphism 😃!")
photo = Instagram("Sunset vibes 🌅")
article = LinkedIn("Why OOP matters in 2025")

start(tweet)
start(photo)
start(article)

"INHERITANCE-BASED POLYMORPHISM"
"In inheritance-based polymorphism, a parent class defines a method, and multiple child classes override that method in their own way. You can then call the same method on any child object, and it behaves differently depending on which child class it is."

"E.g"
class Animal:
    def speak(self):
        return "Some generic sound"
    
class Cat(Animal):
    def speak(self):
        return "A cat meows"
    
class Dog(Animal):
    def speak(self):
        return "A dog barks woof woof"
    
class Monkey(Animal):
    def speak(self):
        return "A monkey ooh ooh aah aah ooh ooh aah aah"
    
# print(Cat().speak())
# print(Dog().speak())
# print(Monkey().speak())
# print(Animal().speak())

# Using a list:
animals = [Cat(), Dog(), Monkey()]

for animal in animals:
    print(animal.speak())


"NAME MANGLING"
"Prefixing an attribute with a double underscore triggers Python's name mangling process, in which Python internally renames the attribute by adding an underscore and the class name as a prefix, turning __attribute into _ClassName__attribute"
class Example:
    def __init__(self, internal, private):
        self._internal = internal
        self.__private = private

example_one = Example(
    "I can be accessed from outside the class, but should not",
    "I cannot be accessed directly from outside the class"
)
example_two = Example(
    'I should not be accessed from outside the class',
    'But I can be accessed from outside the class with name mangling'
)
"PS: You can still access private attribute like this"
print(example_one.__dict__)
print(example_two.__dict__)
print(example_one._Example__private)
print(example_two._Example__private)

"WHY PYTHON DOES NAME MANGLING"
"The main purpose of name mangling is to prevent accidental attribute and method overriding when you use inheritance."

class Parent:
    def __init__(self):
        self.__data = "Parent data"

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__data = "Child data"

c = Child()
print(c.__dict__)

"RULE OF THUMB FOR USING UNDERSCORES"
"""
1. If an attribute is only meant for internal use within the class, stick with a single underscore.

2. But if you're working with a class that will be inherited, you should use a double underscore so the attribute from the parent doesn't get overridden.
"""