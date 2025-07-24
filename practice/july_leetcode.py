"30. Write a Python program that calculates the area of a triangle based on the length, breadth and height entered by the user."

def area_of_triangle(b, h):
    area = 0.5 * b * h
    print(f"Area of triangle is {area}cm2")

# area_of_triangle(5, 10)

from math import pi

"31. What's the circumference of a circle with radius of 5?"
def circumference_of_circle(r:float):
    circ_of_circle = 2 * pi * r
    print(f"The circumference of the circle is {circ_of_circle}")
# circumference_of_circle(4)

"""
32. Write a short program that prints each number from 1 to 100 on a new line. 

For each multiple of 3, print "Fizz" instead of the number. 

For each multiple of 5, print "Buzz" instead of the number. 

For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.

"""
def fizz_buzz():
    for i in range(1, 101):
        if i%3 == 0 and i%5 == 0:
            print("FizzBuzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print(i)
# fizz_buzz()

"""
33. Triple Sum with Equality Rule
Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.
"""
def triple_sum_equality(a, b, c):
    num_sum = a + b + c
    if a == b or a == c or b == c:
        num_sum = 0
    print(f"SUM = {num_sum}")

# triple_sum_equality(6, 2, 6)

""""
Write a program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.
"""
def sum_integ(x:int, y:int):
    int_sum = x + y
    if int_sum in range(15, 21):
        print(20)
        return 20
    else: 
        print(int_sum)
        return int_sum 
    
# sum_integ(1, 7)


"""
35. Equality or 5 Rule Checker
Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.
"""

def equality_or_five(x, y):
    if x == y:
        print(True)
    elif x + y == 5 or x - y == 5:
        print(True)
    elif y - x == 5:
        print(True)
    else:
        print(False)
    
equality_or_five(10, 5)

