"A string is a sequence of characters surrounded by either single or double quotation marks."

my_str_1 = 'Hello'
my_str_2 = "World"

my_str_3 = """Multiline
string"""

"If your string contains either single or double quotation marks, then you have two options:"
"1. Use the opposite kind of quotes. If your string contains single quotes, use double quotes to wrap the string, and vice versa:"

msg = "It's a sunny day!"
quote = 'She said, "Hello World!"'

"2. Escape the single or double quotation mark in the string with a backslash (\). With this method, you can use either single or double quotation marks to wrap the string itself:"

msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""

"IN OPERATOR" # >> Returns a boolean
my_str = 'Hello world'

print("Hello" in my_str)
print("Hey" in my_str)

"LEN METHOD"
print(len(my_str))

"INDEXING"
print(my_str[0])
print(my_str[6])

"NEGATIVE_INDEXING"
print(my_str[-1])
print(my_str[-2])

"Strings are immutable data types in Python. This means that you can reassign a different string to a variable"
"e.g"
greeting = "hi"
greeting = "hello"
print(greeting)

"STRING CONCATENATION & STRING INTERPOLATION"
"1. CONCATENATION"
"In Python, you can combine multiple strings together with the plus (+) operator."

my_str_one = "Hello"
my_str_two = "World"
exclamtn = "!"

str_conc = my_str_one + " " + my_str_two + "" + exclamtn
print(str_conc)

"PS: You can also use the augmented assignment operator for concatenation (+=)"
"e.g"
name = "John Doe"
age = 26

name_age = name + str(age)
# print(name_age)

name_age = name
name_age += str(age)
print(name_age)

"2. STRING INTERPOLATION"
"The process of inserting variables and expressions into a string is called string interpolation."
"f-strings >> Formatted String Literals"

name_and_age = f"My name is {name} and I am {age} years old"
print(name_and_age)


"STRING SLICING"
"SYNTAX: string[start:stop]"
"PS: The value returned includes the 'start' value & excludes the 'stop' value"
print(my_str[0])
print(my_str[6])
print(my_str[-1])

"Note that the 'stop' index is non-inclusive so [1:4] just extracts the characters from index '1' and up to, but not including the character at index 4"
"e.g"
print(my_str[1:4])

print("EMPTY_STR", my_str[5:6])
"PS: When you omit the 'start' and 'stop' indices, Python defaults to 0 or the end of the string respectively"
"e.g"
"This extracts everything from index 0 up to (but not including), the character at index 7. "
print(my_str[:7]) # Hello w

"This extracts everything from the character at index 8 until the end of the string."
print(my_str[8:]) # rld

"PS: You can also omit both the 'start' and 'stop' indices and the entire string will be extracted"
print(my_str[:])

"STEP PARAMETER"
"Apart from the start and stop indices, there's also an optional step parameter, which is used to specify the increment between each index in the slice."
"SYNTAX: string[start:stop:step]"
print(my_str[0:11:2])

"TRICK - Reverse a string 🤪"
print(my_str[::-1])
print(my_str[::-2])

"STRING METHODS"
"upper()"
upper_case_str = my_str.upper()
print(upper_case_str)

