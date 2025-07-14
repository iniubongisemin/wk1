"Write a Python program that calculates the area of a triangle based on the length, breadth and height entered by the user."

def area_of_triangle(b, h):
    area = 0.5 * b * h
    print(f"Area of triangle is {area}cm2")

area_of_triangle(5, 10)

from math import pi

"Q: What's the circumference of a circle with radius of 5?"
def circumference_of_circle(r:float):
    circ_of_circle = 2 * pi * r
    print(f"The circumference of the circle is {circ_of_circle}")
circumference_of_circle(4)
