"LISTS"
"The list data type is an ordered sequence of elements that can be comprised of strings, numbers, or even other lists"
cities = ['Los Angeles', 'London', 'Tokyo']

print(cities[0])
print(cities[-1])

"CONSTRUCTING LISTS"
developer = "Ini-ubong"
print(list(developer))

"UPDATING LISTS"
programming_languages = ['Python', 'Java', 'C++', 'Rust']
programming_languages[0] = "JavaScript"
print(programming_languages)

"DELETING AN ELEMENT FROM A LIST"
developer = ['Jane Doe', 23, 'Python Developer']
del developer[1]
print(developer)

"IN keyword (in)"
print("Rust" in programming_languages)
print("JavaScript" in programming_languages)

"NESTED LISTS"
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
print(developer[2][1])

"UNPACKING VALUES"
developer = ['Inie', 28, 'Backend Developer']
name, age, job = developer
print(name)
print(age)
print(job)

name, *rest = developer
print("NAME>>>>>>", name)
print(rest)
"NB: The number of variable on the left MUST match the number of items in the list!"

"SLICE OPERATOR - ':'"
desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Brownies']
print(desserts[1:4])

"STEP INTERVAL"
numbers = [1, 2, 3, 4, 5, 6] # Extracting "EVEN" numbers
numbers[1::2]
print(numbers[1::3])
"""
The first even number is at index 1, so that will be the start index. Since we want to go through the end of the list, then we omit the end index. Lastly, we specify 2 for the optional step interval so it will only increment by 2 instead of the default 1
"""

"COMMON LIST METHODS"
"APPEND"
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)

"APPENDING ONE LIST TO ANOTHER"
even_numbers = [6, 8, 10]
numbers.append(even_numbers)
print(numbers)

"EXTEND"
numbers.extend(even_numbers)
print(numbers)

"INSERT"
numbers.insert(2, 2.5)
print(numbers)

"REMOVE"
"NB: Only the first occurrence of the item is removed!"
numbers.remove(2.5)
print(numbers)

"POP"
"NB: The number specified is the index of the element to be removed!"
numbers.pop(1)
print(numbers)
"PS: If you don't specify the index of the element to be removed, the last element is popped!"

"CLEAR"
"Empties the list"
# numbers.clear()
print(numbers)

"SORT: Sorts the numbers"
numbers = [19, 2, 35, 1, 67, 41]
numbers.sort()
print(numbers)

"SORTED: Returns a new sorted list rather than modifying the original list"
numbers = [19, 2, 35, 1, 67, 41]
sorted_numbers = sorted(numbers)
print("NUMBERS>>>>>", numbers)
print("SORTED_NUMBERS>>>>>>", sorted_numbers)
"PPS: Both the sort() and the sorted() method accept optional 'key' and 'reverse' parameters"

"REVERSE"
numbers.reverse()
print(numbers)

"INDEX: This is used to find the first index where an element can be found in a list"
print(programming_languages.index("Java"))



"TUPLES"
"Tuples are similar to lists, but while lists are a mutable data type, tuples are immutable. This means that the elements in a tuple cannot be changed once it's created"

"⦿ To access an element from a tuple, you can use bracket notation and the index number"
developer = ("Inie", 28, "Django Developer")
print(developer[0])

"⦿ Tuples also support negative indexing"
numbers = (1, 2, 3, 4, 5)
print(numbers[-2])

"⦿ Another way to create a tuple is by using the tuple() constructor"
# developer = "Ini-ubong"
# print(tuple(developer))

"⦿ IN keyword"
print("Inie" in developer)

"UNPACKING A TUPLE"
name, age, job = developer
print(name)
print(age)
print(job)

"⦿ If you need to collect any remaining elements from a tuple, you can use the asterisk (*) operator"
name, *rest = developer
print(name)
print(rest)

"SLICING A TUPLE"
desserts = ('cake', 'pie', 'cookies', 'ice cream')
print(desserts[1:3])

"PS: 'del' keyword does not work with Tuples!"

"NB: If you are working with data that requires modification, use a LIST. If you are working with fixed data that doesn't require modification, use TUPLES"

"COUNT"
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
print(programming_languages.count("Rust"))

"INDEX"
print(programming_languages.index("Rust"))
"NB: You can specify where to start searching for the string by passing in the start index"
print(programming_languages.index("Python", 1))

"NB: You can also pass in an additional stop index"
programming_languages = ('Rust', 'Java', 'C++', 'Rust', 'Python', 'JavaScript', 'Python')
print(programming_languages.index("Python", 2, 7))

"SORTED"
numbers = (13, 2, 78, 3, 45, 67, 18, 7)
print(sorted(numbers))
"NOTE: The sorted() function will always create a new list of the sorted values. This differs from the sort() method which sorts the elements of a list in place and does not return a new list"
"If you need to customize the sorting behavior for an iterable, you can use the optional reverse and key arguments"

"e.g"
print(sorted(programming_languages, key=len)) # NB: The len function checks the length of each string in the list

"NB: If you want to create a new list of values in reverse order, you can use the reverse argument like this"
print(sorted(programming_languages, reverse=True))



"LOOPS"
"FOR LOOPS"
for language in programming_languages:
    print(language)

for char in "code":
    print(char)

"NESTED 'for' LOOPS"
categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana']

for category in categories:
    for food in foods:
        print(category, food)

"WHILE LOOPS"
"NB: This type of loop will repeat a block of code until the condition is False"
"e.g"
secret_number = 3
guess = 0

while guess != secret_number:
    guess = int(input("Guess the magic number (1-5): "))
    if guess != secret_number:
        print("Wrong guess! Try again")

print("Hurray!!!! You got it")

"BREAK: The break statement is used to stop the execution of a loop"
developer_names = ['Jess', 'Naomi', 'Inie', 'Tom']
for developer in developer_names:
    if developer == "Inie":
        break
    print(developer)

"CONTINUE: The continue statement is used to skip the current iteration of a loop and move onto the next iteration"
for developer in developer_names:
    if developer == "Inie":
        continue
    print(developer)

"NB: Both for and while loops can be combined with an else clause, which is executed only when the loop is not terminated by a break statement"
"e.g"
words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

for word in words:
    for letter in word:
        if letter.lower() in "aeiou":
            print(f"'{word}' contains the vowel '{letter}'")
            break
    else:
        print(f"'{word}' has no vowels")



"RANGE"
"The range() function is used to generate a sequence of integers"
"SYNTAX: range(start, stop, step)"

"e.g"
for num in range(3):
    print(num)
"NB: If a start argument is not specified, then the default is 0"

for num in range(1, 5):
    print(num)

"NB: By default the sequence of integers will increment by 1. But if you want to change that default, then you can use the optional step argument"
for num in range(2, 11, 2):
    print(num)

"NB: The range() function only accepts integers as arguments, not floats"

"DECREMENTING ORDER"
for num in range(50, 0, -10):
    print(num)

"LIST CONSTRUCTOR"
numbers = list(range(2, 11, 2))
print(numbers)



"ENUMERATE & ZIP FUNCTIONS"
"e.g Keeping track of the index of each element"
"Conventional Method"
languages = ['Spanish', 'English', 'Russian', 'Chinese']
index = 0

for lang in languages:
    print(f"Index {index} and language {lang}")
    index += 1

"USING ENUMERATE"
"The enumerate() function keeps track of the index for an iterable and returns an enumerate object"
print(list(enumerate(languages))) # [(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')]

"Refactoring the Conventional Method"
for index, language in enumerate(languages):
    print(f"Index {index} and language {language}")

"PS: The enumerate() function also accepts an optional start argument that specifies the starting value for the count"
"e.g"
for index, language in enumerate(languages, 1):
    print(f"Index {index} and language {language}")

"ZIP"
"Used when you need to iterate over multiple iterables in parallel"
developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

print(list(zip(developers, ids)))

"Zip in a for loop"
for name, id in zip(developers, ids):
    print(f"Name: {name}")
    print(f"ID: {id}")


"LIST COMPREHENSION"
"e.g Without List Comprehension"
even_numbers = []

for num in range(21):
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)

"e.g With List Comprehension"
even_numberz = [num for num in range(21) if num % 2 == 0]
print("EVEN_NUMBERZ: ", even_numberz)

"Ex2"
numbers = [1, 2, 3, 4, 5]
result = [(num, "Even") if num % 2 == 0 else (num, "Odd") for num in numbers]
print(result)

"FILTER FUNCTION: Used to select elements from an iterable that meet a specific condition"
"SYNTAX: filter(func, iterable)"
"Ex3: Creating a list using filter()"
words = ["tree", "sky", "mountain", "river", "cloud", "sun"]
def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word, words))
print(long_words)

"MAP: Takes an iterable and applies a function to each of its elements"
"Ex4"
celsius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
    return (temp * 9/5) + 32

fahrenheit = list(map(to_fahrenheit, celsius))
print(fahrenheit)

"SUM"
total = sum(celsius)
print("TOTAL", total)
"NB: You can also pass in an optional start argument which sets the initial value for the summation"
total = sum(celsius, 20)
print("TOT: ", total)

