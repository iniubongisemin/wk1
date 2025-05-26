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
# print(concat_list_with_space(li_sts))

word_list = ["alpha", "bravo", "charlie", "echo", "delta", "foxtrot"]
"""
Write a function that joins a list of strings into a single string but reverses each individual word before joining.
"""
def join_reverse(listt:list):
    all_str = ""
    for i in listt:
        x = i[::-1]
        all_str += x
    print(all_str)
# join_reverse(word_list)

"""
Write a Python program to concatenate elements from a list, separating numbers and letters into different sections.
"""
lit = [11, 21, 31, 41, 51, 61, 71, 81, 91, 101, "a", "e", "i", "o", "u"]

def list_str(listt):
    all_list_string = []
    strng = ""
    integer = ""

    for i in listt:
        if isinstance(i, str):
            strng += i
        if isinstance(i, int):
            j = str(i)
            integer += j
    all_list_string.append(integer)
    all_list_string.append(strng)
    print(all_list_string)
list_str(lit)