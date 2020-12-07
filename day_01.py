"""
12/06/2020
Day 1 - Part 1
Find the two entries that sum to 2020 and then multiply those two numbers together.
"""

result = []
with open('day_01.txt') as f:
    lst = [int(i.strip('\n')) for i in list(f)]
    for x in lst:
        y = 2020 - x
        if y in lst:
            result.append(x*y)
print(set(result))
