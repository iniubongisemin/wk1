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

    def get_balace(self):
        return self.__balance
    
account = Wallet(500)
print(f"Here's your account balance ₦{account.get_balace()}")

account.deposit(100000)
print(f"Here's your account balance ₦{account.get_balace()}")

account.withdraw(25000)
print(f"Here's your account balance ₦{account.get_balace()}")

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
        