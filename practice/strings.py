# python strings
# you can display strings with print() function 
# print('hello')
# print("hello")

# assigning string to a variable 
s = 'string'
# print(s)

# multiline strings
# use three (double or single) quotes
lorem = '''lorem ipsum dolor sit amet'''
# print(lorem)

prodev = """i \nlove \ncoding"""  # \n is used as a line break
# print(prodev)

# NB: strings are arrays of bytes representing unicode characters
first_line_of_code = 'hello world'
# print(first_line_of_code)

# looping through a string
# since strings are arrays, we can loop through the characters in a string with a for loop
# e.g loop through the letters in the word banana
for x in 'banana':
    pass
    print(x)

# string length len()
ini = 'software engineer'
print(len(ini))

# check string - "in"
txt = 'the best things in life are not free!'
print('free' in txt) 

# using "in" in an if statement
if 'free' in txt:
    print('yes! free is present in text.')
    pass

# check if NOT using "not in"
# to check if a certain phrase is NOT present in a string, use the keyword "not in"
# e.g check if "expensive" is NOT present in the following text:
# print("expensive" not in txt)

# using it in an if statement 
if "expensive" not in txt:
    print('No, "expensive" is NOT present in txt.')
    pass

# slicing strings
# you can return a range of characters by using the slice syntax
# e.g get the characters from position 2 to position 5(not included)
code = 'HELLO, WORLD!'
print(code[2:5])
print(len(code))

# slice from the start: by leaving out the start index, the range automatically starts at the first character
# e.g get the characters from the start to position 5(not included)
print(code[:5])
print(code[5:])

# slice to the end: by leaving out the end index, the range automatically goes to the end;
# e.g get the characters from position 2 all the way to the end
# print(code[2:])

# negative indexing: used to start the slice from the end of the string;
# e.g get the characters "O" in "WORLD!" (position -5) to, but not included: "D" in "world" (position -2)
print(code[-5:-2])

# modifying strings
# upper()
print(code.upper())

# lower()
print(code.lower())

# capitalize()
print(code[7].capitalize())
print(code.capitalize())

# removing whitespace
coder = ' hello world! '
print(coder.strip())

# replace string: the replace method replaces a string with another string
print(code.replace('L', 'S'))

if 'l' in code:
    print('yes l is present in code')

else:
    print('oops l is not present in code')

# split() string method: returns a list where the text between the specified separator becomes the list items 
print(coder.split(" "))

# python string methods reference
# NB: all string methods return new values, they do not change the orignal string

#1. capitalize() - converts the first character to upper case e.g
# NB: only the first character is converted to uppercase, the other characters are converted to lower case 
print(code.capitalize())

#2. casefold() - converts all characters to lower case, it's similar to lower(), but its stronger 
school = 'UNIVELCITY'
print(school.casefold())

#3. center() - returns a centred string 
lifeQuoute = 'with God, nothing is impossible'

#4. count() - returns the number of times a specified value occurs in a string
print(lifeQuoute.count('s'))

#5. encode() - returns an encoded version of the string
print(lifeQuoute.encode)

#6. endswith() - return True if the string ends with the specified value


#7. expandtabs() - sets the tab size of the string


#8. find() - searches the string for a specified value and returns the position of where it was found


#9. format() - formats specified values in a string 


#10. format_map() - formats specified values in a string


#11. index() - searches the string for a specified value and returns the position of where it was found


#12. isalnum() - returns True if all the characters in the string are alphanumeric 


#13. isalpha() - returns True if all the characters in the string are alphabets


#14. isascii() - returns True if all the     ''     '' ''    ''    ''  ascii characters 


#15. isdecimal() - returns True if all the characters in the string are decimals


#16. isdigit() - returns True if all the characters in the string are digits


#17. isIdentifier() - returns True if the string is an identifier


#18. isnumeric() - returns True if all characters in the string are nummeric


#19. isprintable() - returns True if all characters in the string are printable


#20. isspace() - returns True if all characters in the string are whitespaces


#21. istite() - returns True if the string follows the rules of a title


#22. join() - converts the elements of an iterable into a string 


#23. ljust() - returns a justified version of the string


#24. lstrip() - returns a left trim version of the string


#25. maketrans() - returns a translation table to be used in translations


#26. partition() - returns a tuple where the string is parted into three parts


#27. replace() - returns a string where a specified value is replaced with a specified value


#28. rfind() - searches the string for a specified value and returns the last position of where it was found


#29. rindex() - searches the string for a specified value and returns the last position of where it was found


#30. rjust() - returns a right justified version of the string


#31. rpartition() - returns a tuple where the string is parted into three parts


#32. rsplit() - returns a list where the text between the specified separator becomes the list items


#33. rsplitlines() - splits the string at the breaks and returns a list


#34. strip() - returns a trimmed version of the string


#35. swapcase() - swaps cases, lower case becomes upper case and vice versa


#36. title() - converts the first character of each word to uppercase


#37. translate() - returns a translated string


#38. zfill() - fills the string with a specified number of 0 values at the beginning 

