"""
12/06/2020
Day 1 - Part 1
Find the two entries that sum to 2020 and then multiply those two numbers together.
"""

import numpy as np

result = []
with open('day_01.txt') as f:
    lst1 = [int(i.strip('\n')) for i in list(f)]
    lst2 = [2020 - j for j in lst1]
    for y in lst2:
        if y in lst1:
            result.append(y)
print(f'The two entries are: {result}')
print(f'Their product is : {np.prod(result)}')

"""
12/06/2020
Day 1 - Part 2
Find the three entries that sum to 2020 and then multiply those three numbers together.
"""
import numpy as np

result = []
with open('day_01.txt') as f:
    lst1 = [int(i.strip('\n')) for i in list(f)]
    lst2 = [2020 - j for j in lst1]
    for x in lst1:
        for y in lst2:
            z = y - x
            if z in lst1:
                result.append(z)
print(f'The three entries are: {list(set(result))}')
print(f'Their product is : {np.prod(list(set(result)))}')
