def is_palindrome(s: str) -> bool:
    l, r = 0, len(s)-1

    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True

if __name__ == "__main__":
    s = input("Please type your string: ")
    res = is_palindrome(s)
    print("True" if res else "False")






# def is_palindrome(s: str) -> bool:
#     l, r = 0, len(s)-1

#     while l < r:
#         while l < r and not s[l].isalnum():
#             l += 1
#         while l < r and not s[r].isalnum():
#             l += 1
#         if s[l].lower() != s[r].lower():
#             return False
#     l += 1
#     r += 1 

#     return True

# if __name__ == "__main__":
#     s = input("Please type your string: ")
#     result = is_palindrome(s)
#     print("True" if result else "False")

r1 = [2, 4, 6, 8]
r2 = [1, 2, 3, 4, 5, 6]


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

    print(intersection)

if __name__ == "__main__":
    intersect_sorted(r1, r2)