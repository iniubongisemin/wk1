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

"IN keyword"
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
print(name)
print(rest)
"NB: The number of variable on the left MUST match the number of items in the list!"

"SLICE OPERATOR - ':'"
desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Brownies']
print(desserts[1:4])

"STEP INTERVAL"
numbers = [1, 2, 3, 4, 5, 6] # Extracting "EVEN" numbers
numbers[1::2]
"""
The first even number is at index 1, so that will be the start index. Since we want to go through the end of the list, then we omit the end index. Lastly, we specify 2 for the optional step interval so it will only increment by 2 instead of the default 1
"""

