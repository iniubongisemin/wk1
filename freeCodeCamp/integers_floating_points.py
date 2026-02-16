"All Arithmetic Methods Hold"
"MODULUS" # Modulus >> Remainder from division
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

mod_ints = my_int_1 % my_int_2
mod_floats = my_float_2 % my_float_1

print("Integer Modulus: ", mod_ints) 
print("Float Modulus: ", mod_floats)

"FLOOR DIVISION"
floor_div_ints = my_int_1 // my_int_2
floor_div_floats = my_float_2 // my_float_1

print("Integer Floor Division: ", floor_div_ints)
print("Float Floor Division: ")

"EXPONENTIATION"

exp_ints = my_int_1 ** my_int_2
exp_floats = my_float_1 ** my_float_2

print("Integer Exponentiation: ", exp_ints)
print("Float Exponentiation: ", exp_floats)

"IN-BUILT METHODS FOR WORKING WITH INTEGERS & FLOATS"
"ROUND()" # Rounds a number to the specified number of decimal places -- By default it rounds to the nearest integer & returns a whole number with no decimal places!
my_int_1 = 4.798
my_int_2 = 4.253

rounded_int_1 = round(my_int_1)
rounded_int_2 = round(my_int_2, 1)

print(rounded_int_1)
print(rounded_int_2)

"ABS()" #Returns the absolute value of a number
num = -15
absolute_value = abs(num)
print(absolute_value)

"POW()" # Raises a number to the power of another or performs modular exponentiation
result_1 = pow(2,3)
result_2 = pow(2,3, 5)

print(result_1)
print(result_2)




