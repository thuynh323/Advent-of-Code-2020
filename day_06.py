"""
12/09/2020
Day 6: Custom Customs
"""

#*************************************************************************************************#
# Part 1: For each group, count the number of questions to which anyone answered "yes".           #
# What is the sum of those counts?                                                                #
#*************************************************************************************************#

import re
def count_char(lines):
    count = 0
    for l in lines:
        char = set(re.findall(r'\w', l))
        count += len(char)
    return count
        
with open('day_06.txt') as f:
    lst1 = f.read().split('\n\n')
    lst2 = []
    for l in lst1:
        val = l.split('\n')
        lst2.append(''.join(val))
    print(f'Number of answers: {count_char(lst2)}')
    
#*************************************************************************************************#
# Part 2: For each group, count the number of questions to which everyone answered "yes".         #
# What is the sum of those counts?                                                                #
#*************************************************************************************************#

def count_question(groups):
    count = 0
    for g in groups:
        num_mem = len(g)
        all_q =  ''.join(g)
        char = list(set(re.findall(r'\w', all_q)))
        for i in range(0, len(char)):
            if all_q.count(char[i]) == num_mem:
                count += 1
    return count

with open('day_06.txt') as f:
    lst = f.read().split('\n\n')
    group_mem = []
    for l in lst:
        group_mem.append(l.strip('\n').split('\n'))
    print(f'Number of questions answered by every member: {count_question(group_mem)}')
