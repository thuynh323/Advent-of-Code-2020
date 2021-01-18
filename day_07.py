"""
12/12/2020
Day 7: Handy Haversacks
"""

import re
def get_rules(rules):
    bag_dict, all_bags = {}, {}
    for r in rules:
        container = re.findall(r'^\S+\s\S+(?= bags contain [0-9])', r)
        if container:
            parent = container[0]
            child_list = re.findall(r'(?<=[0-9] )\S+\s\S+', r)
            bag_dict[parent] = child_list
            num_list = re.findall(r'\d+', r)
            number = list(map(int, num_list))
            all_bags[parent] = dict(zip(child_list, number))   
        else:
            continue 
    return bag_dict, all_bags

# bag_dict = {'pale cyan': ['posh black', 'wavy gold', 'vibrant brown'], 'dull lavender': ['pale tomato'],...}
# all_bags = {'pale cyan': {'posh black': 2, 'wavy gold': 4, 'vibrant brown': 2}, 'dull lavender': {'pale tomato': 3},...}

#*************************************************************************************************#
# Part 1: How many bag colors can eventually contain at least one shiny gold bag?                 #
#*************************************************************************************************#
 
def count_parents(rules, color):
    bag_dict = rules[0]
    parent = [outer for outer, inner in bag_dict.items() if color in inner]     
    for p in parent:
        for outer, inner in bag_dict.items():
            if p in inner:
                parent.append(outer)
    count = len(set(parent))   # Different outer bags may be contained in the same bag
    return count

#*************************************************************************************************#
# Part 2: How many individual bags are required inside your single shiny gold bag?                #
#*************************************************************************************************#

def count_children(rules, color):
    all_bags = rules[1]
    count = 1
    if color in all_bags:
        children = all_bags[color]
        for c in children:
            multiplier = children[c]
            count += multiplier*count_children(rules, c)
    return count

with open('day_07.txt') as f:
    lst = [x.strip('\n') for x in f.readlines()]
    rules = get_rules(lst)
    print(f"Number of bags that can contain at least one shiny gold bag: {count_parents(rules, 'shiny gold')}")
    print(f"Number of bags that can be contained by one shiny gold bag: {count_children(rules, 'shiny gold') - 1}")
