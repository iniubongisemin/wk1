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
    pass