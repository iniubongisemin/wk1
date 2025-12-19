"O(n2)"
chars = "learning"
result = ""
for char in chars:
    result += char

# print(result) 

"O(n)"
result = []
for char in chars:
    result.append(char)

# print("".join(result))
# words = ["l", "e", "a", "r", "n", "i", "n", "g"]
# print("".join(words))

"SETS"
nums = [1, 2, 3, 4, 5]
seen = set(nums)
print(3 in seen)

"""WHEN TO USE A SET INSTEAD OF A LIST"""
"1. When uniqueness matters"
"2. Checking for Existence"
"3. Fast membership checks"
"4. Sliding window"
"PS: You'll use sets way more than lists in your solutions"
"PPS: Always practice walking through your solution with dummy data"

"https://chatgpt.com/s/t_69133ad921388191888a07f877948ca6"

def fibonacci_algorithm():
    fib_list = []
    a = b = 0
    while len(fib_list) < 21:
        fib_num = a + b
        fib_list.append(fib_num)
        if len(fib_list) == 1:
            b += 1
        a = b
        b = fib_num
    print("FIBONACCI SEQUENCE: ", fib_list)
fibonacci_algorithm()

"""
JIT Learning for DSA
1. Arrays
2. Linked Lists
3. Stacks
4. Queues
5. Binary Trees
6. Hash Tables
7. Heaps 
8. Graphs

Additionally 
9. Union Find
10. Trees
"""