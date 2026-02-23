print(3 > 4) # False
print(3 < 4) # True
print(3 == 4) # False
print(4 == 4) # True
print(3 != 4) # True
print(3 >= 4) # False
print(3 <= 4) # True

# In Python, the most basic conditional is the if statement.
x = 4 
condition = True if x > 4 else False

"SYNTAX"
if condition:
    pass

age = 18

if age >= 18:
    print("You are an adult 😋")

"IF ELSE STATEMENTS"
if condition:
   pass 
else:
   pass 

if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")

"PS: You can chain multiple elif statements before ending with an else statement"

"TRUTHY, FALSY VALUES, BOOLEAN OPERATORS & SHORT CIRCUITING"
"FALSY VALUES"
'* None'
'* False'
'* Integer 0'
'* Float 0.0'
'* Empty strings ""'
"NB: Other values like non-zero numbers, and non-empty strings are truthy."
# Falsy
print(bool(False))
print(bool(0))
print(bool(""))
# Truthy
print(bool(True))
print(1)
print("Hello")

"BOOLEAN OPERATORS"
"*AND"
"*OR"
"*NOT"

"The and operator takes two operands and returns the first operand if it is falsy, otherwise, it returns the second operand. Both operands must be truthy for an expression to result in a truthy value."
is_citizen = True
age = 25

print(is_citizen and age)
"SHORT CIRCUITING"
"Short-circuiting means Python checks values from left to right and stops as soon as it determines the final result."

is_citizen = True
age = 25

"AND"
if is_citizen and age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

"OR"
age = 19
is_employed = False
is_student = True

print(age or is_employed)

if age < 18 or is_student:
    print("You are eligible for a student discount")
else:
    print("You are eligible for a student discount")

"NOT"
"Takes a single operand and inverts its boolean value i.e converts 'truthy' values to False and 'falsy' values to True"
"PS: 'not' always returns 'True' or 'False'"

print(not '') # True, because empty strings are falsy
print(not "Hello") # False, because non-empty string
print(not 0) # True, because 0 is falsy
print(not 1) # False, because 1 is truthy
print(not False) # True, because False is falsy
print(not True) # False, because True is truthy

is_admin = False

if not is_admin:
    print("Access denied for non-administrators")
else:
    print("Welcome, Administrator!")

"ORDER OF LOGICAL OPS"
"""When multiple logical operators are used in an if statement, conditions joined with 'and' are evaluated before conditions joined with or. Parentheses () are used in Python to group conditions and control the order in which they are evaluated."""

"NESTED IFs"
"#WORKSHOP"

base_price = 15
age = 21
seat_type = 'Gold'
show_time = 'Evening'

if age > 17:
    print('User is eligible to book a ticket')

if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

is_member = False
is_weekend = False

discount = 0
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

extra_charges = 0
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print('Service charges:', service_charges)
    final_price = (base_price + extra_charges + service_charges) - discount
    print('Final price of ticket:', final_price)
else:
    print('Ticket booking failed due to restrictions')
