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
    lst = []
    for l in lines:
        val = l.split('\n')
        lst.append(''.join(val))
    
    count = 0
    for i in lst:
        char = set(re.findall(r'\w', i))
        count += len(char)
    return count
    
#*************************************************************************************************#
# Part 2: For each group, count the number of questions to which everyone answered "yes".         #
# What is the sum of those counts?                                                                #
#*************************************************************************************************#

def count_question(lines):
    groups = []
    for l in lines:
        groups.append(l.strip('\n').split('\n'))
    
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
    print(f'Number of answers: {count_char(lst)}')
    print(f'Number of questions answered by every member: {count_question(lst)}')
