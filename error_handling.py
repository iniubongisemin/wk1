# DEBUGGING
"Good Debugging Techniques in Python"

"1. Using the print function and f-strings"
def add(a, b):
    result = a + b
    print(f"Adding {a} and {b} gives {result}")
    return result

# add(5, 40)

"2. Interactive Debugging with the pdb Module"
# import pdb
# def divide(a, b):
#     pdb.set_trace()
#     return a / b
# print(divide(10, 2))

"3. IDE Debugging Tools"
"USING VS CODE DEBUGGER: > Add a break point > Click Run & Debug button on the tool bar on the left"
# Use the debug toolbar to:
# 1. Continue (F5): Resume execution until the next breakpoint
# 2. Step Over (F10): Execute the current line and move to the next
# 3. Step Into (F11): Enter into function calls
# 4. Step Out (Shift+F11): Exit the current function

def divide(a, b):
    result = a / b
    return result

print(divide(10, 2))
print(divide(15, 3))

# Each technique has its place: 
# print() statements for quick checks 
# pdb for interactive exploration, and 
# IDE debuggers for visual inspection.


"HOW EXCEPTION HANDLING WORKS"
"Python provides:"
"1. try"
"2. except"
"3. else"
"4. finally" # This runs regardless of exceptions, useful for closing connections, resources, files etc.

"TRY ~ EXCEPT"
try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

"ELSE ~ FINALLY"
try:
    x = 10 / 2
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("Division successful: ", x)
finally:
    print("This block always runs.")

"MULTIPLE EXCEPT BLOCKS"
try:
    number = int("abc")
    result = 10 / number
except ValueError:
    print("That was not a valid number!")
except ZeroDivisionError:
    print("Can't divide by zero.")

"USING THE EXCEPTION OBJECT"
try:
    x = 1 / 0 
except ZeroDivisionError as e:
    print(f"An exception occured: {e}")

"CATCHING MULTIPLE EXCEPTIONS IN A SINGLE EXCEPT CLAUSE" # You do this by specifying the exception as a tuple!

try:
    number = int(input("Enter a number: "))
    result = 10 / number
except (ValueError, ZeroDivisionError) as e:
    print(f"An error occurred: {e}")

"THE RAISE STATEMENT"
"The raise statement is a powerful tool that allows you to manually trigger exceptions in your code."
'E.g'

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    return age

try:
    check_age(-5)
except ValueError as e:
    print(f"Error: {e}")

"NB: The raise statement can also be used to re-raise the current exception, which is particularly useful in exception handling"

def process_data(data):
    try:
        result = int(data)
        return result * 2
    except ValueError:
        print("Logging: Invalid data received")
        raise

try:
    process_data("abc")
except ValueError:
    print("Handled at higher level")

# You can create and raise custom exceptions by defining your own exception classes:

class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: ₦{balance} available, ₦{amount} requested")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except InsufficientFundsError as e:
    print(f"Transaction failed: {e}")

"NB: The raise statement can also be used with the 'from' keyword to chain exceptions, showing the relationship between different errors"
def parse_config(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            return int(data)
    except FileNotFoundError:
        raise ValueError("Configuration file is missing!") from None
    except ValueError as e:
        raise ValueError("Invalid configuration format!")
    
# config = parse_config("config.txt")

"PS: You can also raise exceptions conditionally using assert statements, which are essentially shorthand for raise with AssertionError"

def calculate_square_root(number):
    assert number >= 0, "Cannot calculate square root of negative number"
    return number ** 0.5

try:
    result = calculate_square_root(-4)
except AssertionError as e:
    print(f"Assertion failed: {e}")
