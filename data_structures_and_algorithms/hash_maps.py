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