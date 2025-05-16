"""
27. List to String Concatenator
Write a Python program that concatenates all elements in a list into a string and returns it.
"""
li_sts = [11, 21, 31, 41, 51, 61, 71, 81, 91, 101]
def list_to_string(listt:list):
    result = ''
    for i in listt:
        result += str(i)
    return result
# print(list_to_string(li_sts))

"""
Extra: Write a Python program to concatenate all elements in a list but insert a space between each element.
"""
def concat_list_with_space(lis:list):
    result = ''
    for i in lis:
        j = str(i)
        result += j+"✅"
    return result
print(concat_list_with_space(li_sts))
"""
Write a function that joins a list of strings into a single string but reverses each individual word before joining.
"""