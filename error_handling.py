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