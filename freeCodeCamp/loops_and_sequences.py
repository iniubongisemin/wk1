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




