"Common Data Types in Python"
"INTEGER"
my_integer_var = 10
print('Integer:', my_integer_var) # Integer: 10

"FLOAT"
my_float_var = 4.50
print('Float:', my_float_var) # Float: 4.5

"STRING"
my_string_var = 'hello'
print('String:', my_string_var) # String: hello

"BOOLEAN"
my_boolean_var = True
print('Boolean:', my_boolean_var) # Boolean: True

"SET"
my_set_var = {7, 5, 8}
print('Set:', my_set_var) # Set: {7, 5, 8}

"DICTIONARY"
my_dictionary_var = {"name": "Alice", "age": 25}
print('Dictionary:', my_dictionary_var) # Dictionary: {'name': 'Alice', 'age': 25}

"TUPLE"
my_tuple_var = (7, 5, 8)
print('Tuple:', my_tuple_var) # Tuple: (7, 5, 8)

"RANGE"
my_range_var = range(5)
print(my_range_var) # range(0, 5)

"LIST"
my_list = [22, 'Hello world', 3.14, True]
print(my_list) # [22, 'Hello world', 3.14, True]

"NONE"
my_none_var = None
print('None:', my_none_var) # None: None

"IMMUTABLE TYPES"
"integer, float, complex, boolean, string, tuple, range, and Non"

"MUTABLE TYPES"
"list, set, and dictionary"

"ISINSTANCE"
greeting = 'Hello world'
name = 'John Doe'

print(isinstance(greeting, str)) # True
print(isinstance(name, int)) # False

"ACCESSING CHARACTERS FROM STRINGS"
my_str = 'Hello world'

print(my_str[0])  # H
print(my_str[6])  # w

print(my_str[-1])  # d
print(my_str[-2]) # l

"STRING CONCATENATION"
developer = 'Inie'
print('My name is' + developer + '.') # My name is Inie.

"STRING SLICING"
"str[start:stop:step]"

message = 'Python is fun!'

print(message[0:6])  # Python
print(message[7:])  # is fun!
print(message[::2])  # Pto sfn

"IN OPERATOR"
my_str = 'Hello world'

print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False

"COMMON STRING METHODS"
"str.strip()"
greeting = '  hello world  '

trimmed_my_str = greeting.strip()
print(trimmed_my_str)  # 'hello world'

"replace()"
greeting = 'hello world'

replaced_my_str = greeting.replace('hello', 'hi')
print(replaced_my_str)  # 'hi world'

"split()"
dashed_name = 'example-dashed-name'

split_words = dashed_name.split('-')
print(split_words)  # ['example', 'dashed', 'name']

"join()"
example_list = ['example', 'dashed', 'name']

joined_str = ' '.join(example_list)
print(joined_str)  # example dashed name

"str.startswith(prefix)"
developer = 'Naomi'

result = developer.startswith('N')
print(result)  # True

"str.endswith(suffix)"
developer = 'Naomi'

result = developer.endswith('N')
print(result)  # False

"str.find()"
developer = 'Naomi'

result = developer.find('N')
print(result)  # 0

city = 'Los Angeles'
print(city.find('New')) # -1

"str.count(substring)"
city = 'Los Angeles'
print(city.count('e')) # 2

"str.isupper()"
dessert = 'chocolate cake'
print(dessert.isupper()) # False

"str.islower()"
dessert = 'chocolate cake'
print(dessert.islower()) # True

"str.title()"
city = 'los angeles'
print(city.title()) # Los Angeles

"str.maketrans()"
trans_table = str.maketrans('abc', '123')
print(trans_table) # {97: 49, 98: 50, 99: 51}

result = 'abcabc'.translate(trans_table)
print(result)  # 123123

"NUMBERS"
"Modulus Operator"





