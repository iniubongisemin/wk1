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
    str_count = 0
    int_count = 0

    for i in listt:
        if isinstance(i, str):
            strng += i
            str_count += 1

        if isinstance(i, int):
            j = str(i)
            integer += j
            int_count += 1
    all_list_string.append(integer)
    all_list_string.append(strng)
    print(all_list_string, f"INTEGER_COUNT: {int_count}, STRING_COUNT: {str_count}")
# list_str(lit)

"""
28. Even Numbers Until 237
Write a Python program to print all even numbers from a given list of numbers in the same order and stop printing any after 237 in the sequence.
Sample numbers list :
"""
sample_numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

def even_num_till(number:list):
    for i in number:
        if i != 237:
            print(i)
        else:
            continue
even_num_till(sample_numbers)

"""
29. Unique Colors Finder
Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}
"""
color_list_1 = set(["White", "Black", "Red"])
color_list_1 = list(color_list_1)
# color_list_1 = color_list_1[0]
# print(color_list_1)
color_list_2 = set(["Red", "Green"])
color_list_2 = list(color_list_2)
# color_list_2 = color_list_2[0]
# print(color_list_2)
def unique_colors_finder(c_list1:list, c_list2:list):
    for i in c_list1:
        if i not in c_list2:
            print(i)
# unique_colors_finder(color_list_1, color_list_2)

"""
30. Triangle Area Calculator
Write a Python program that will accept the base and height of a triangle and compute its area.
"""
b = 4
h = 2
def area_of_triangle(b, h):
    a = 1/2 * b * h
    print(a)
area_of_triangle(b, h)

