"""BASIC CODE STRUCTURE FOR HASH MAPS PROBLEMS"""
"Frequency Map"
my_map = {}
data = {}

for item in data:
    if item not in my_map:
        my_map[item] = 1
    else:
        my_map[item] += 1

from collections import defaultdict

"""TWO SUM"""
"Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target. You may assume that each input will have exactly one solution, and you may not use the same element twice!"
"e.g"
"Input: nums = [2, 7, 11, 15], target = 9"
"Output: [0, 1]"
"Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]"

def two_sum(arr: list[int], target: int) -> list[int]:
    num_to_index = {}

    for i, num in enumerate(arr):
        complement = target - num

        if complement in num_to_index:
            return [num_to_index[complement], i]
        
        num_to_index[num] = i
    return []

"ANALYSE THE SPACE ~ TIME COMPLEXITY"
def two_sum(arr: list[int], target: int) -> list[int]:
    s: dict[int, int] = {} # ->> THIS IS THE HASH MAP
    for i, num in enumerate(arr):
        if target - num in s:
            return [s[target - num], i]
        s[num] = i
    return []
    
if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = two_sum(arr, target)
    print("".join(map(str, res)))