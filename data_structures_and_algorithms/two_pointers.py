"""
Find the intersection between two sorted arrays in Python.
"""
def intersect_sorted(arr_one, arr_two):
    i, j = 0, 0
    intersection = []

    while i < len(arr_one) and j < len(arr_two):
        if arr_one[i] == arr_two[j]:
            intersection.append(arr_one[i])
            i += 1
            j += 1
        elif arr_one[i] < arr_two[j]:
            i += 1
        else:
            j += 1
    
    return intersection

"USING SET APPROACH"
def set_intersection(arr_one, arr_two):
    array_one = set(arr_one)
    array_two = set(arr_two)

    intersect = array_one.intersection(array_two)

    return intersect
