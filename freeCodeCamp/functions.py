"SCOPE IN PYTHON"

"""
To correctly determine scope, Python follows the LEGB rule, which stands for the following:

⦿ Local scope (L): Variables defined in functions or classes.
⦿ Enclosing scope (E): Variables defined in enclosing or nested functions.
⦿ Global scope (G): Variables defined at the top level of the module or file.
⦿ Built-in scope (B): Reserved names in Python for predefined functions, modules, keywords, and objects.
"""

"LOCAL SCOPE: Means that a variable declared inside a function or class can only be accessed within that function or class."
def my_func():
    my_var = 10 # Locally scoped to my_func
    print(my_var)

my_func() # 10

# print(my_var) # NameError: name 'my_var' is not defined

"ENCLOSING SCOPE: Means that a function that's nested inside another function can access the variables of the function it's nested within."
def outer_func():
    msg = 'Hello there!'

    def inner_func():
        print(msg)

    inner_func()

outer_func() # Hello there!
"NB: However, note that outer functions cannot access variables defined within any nested functions"

def outer_func():
    msg = 'Hello there!'
    # print(res)

    def inner_func():
        res = 'How are you?'
        print(msg)

    inner_func()

outer_func() # NameError: name 'res' is not defined

"""One solution is to initialize res as an empty string in the enclosing scope, which is within outer_func. Then within inner_func, make res a non-local variable with the nonlocal keyword:"""
def outer_func():
    msg = "Hello there!"
    res = "" # Declare res in the enclosing scope

    def inner_func():
        nonlocal res # Allow modification of an enclosing variable
        res = "How are you?"
        print(msg)

    inner_func()
    print(res)

outer_func()

"GLOBAL SCOPE: Refers to variables that are declared outside any functions or classes which can be accessed from anywhere in the program."
my_var = 100

def show_var():
    print(my_var)

show_var() # 100
print(my_var) # 100

"PS: If you want to make a locally scoped variable defined inside a function globally accessible, you can use the global keyword"
my_var_1 = 7 

def show_vars():
    global my_var_2
    my_var_2 = 10
    print(my_var_1)
    print(my_var_2)

show_vars()

print(my_var_2)

"PPS: You can also use the 'global' keyword to modify a global variable"
my_var = 10

def change_var():
    global my_var
    my_var = 20

change_var()

print(my_var)

"BUILT-IN-SCOPE: Refers to all of Python's built-in functions, modules, and keywords, and are available anywhere in your program"


def apply_discount(price: int | float, discount: int | float): # WRONG APPROACH
    if not isinstance(price, int) or not isinstance(price, float):
        # raise ValueError("The price should be a number")
        return "The price should be a number"
    else:
        pass

    if not isinstance(discount, int) or not isinstance(discount, float):
        raise ValueError("The discount should be a number")
        # return "The discount should be a number"
    else:
        pass

    if price <= 0:
        return "The price should be greater than 0"

    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"
    
    else:
        final_price = price * (discount/100)
        return f"FINAL_PRICE: {final_price}"
    
apply_discount(100, 20)

"CORRECTION"
def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        return "The price should be a number"
    elif not isinstance(discount, (int, float)):
        return "The discount should be a number"
    elif price <= 0:
        return "The price should be greater than 0"
    elif discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"
    else:
        final_price = price * (1 - discount/100)
    return final_price

print(apply_discount(1000, 20))

"""
The Mathematical Breakdown
When you apply a discount, you are essentially taking the "Whole" (100%) and removing a "Part" (the discount).
The "Whole": Represented by the number 1 (which is 100%).
The "Part": Represented by discount/100 (e.g., $0.20$ for a $20\%$ discount).
If you use your original formula, price * (discount / 100), you are calculating the savings: $100 * 0.20 = 20 (You saved $20).
If you use the new formula, price * (1 - discount / 100), you are calculating the final price: $100 * (1 - 0.20) > 100 * 0.80 = 80 (You pay $80).
"""
