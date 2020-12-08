"""
12/07/2020
Day 3: Toboggan Trajectory
"""

#*************************************************************************************************#
# Part 1: From your starting position at the top-left, check the position that is                 #
# right 3 and down 1. Then, check the position that is right 3 and down 1 from there, and so on   #
# until you go past the bottom of the map. How many trees (#) would you encounter?                #
# The provided file is not a complete map. Each line has the same pattern repeats                 #
# to the right many times.                                                                        #
#                                                                                                 #
# Part 2: Determine the number of trees you would encounter if, for each of the following slopes, #
# you start at the top-left corner and traverse the map all the way to the bottom:                #
# - Right 1, down 1.                                                                              #
# - Right 3, down 1. (This is the slope you already checked.)                                     #
# - Right 5, down 1.                                                                              #
# - Right 7, down 1.                                                                              #
# - Right 1, down 2.                                                                              #
# What do you get if you multiply together the number of trees encountered                        #
# on each of the listed slopes?                                                                   #
#*************************************************************************************************#

def count_tree(lines, down: 'int', right: 'int'):
    x = 0
    run = 0
    width = len(lines[0])
    height = len(lines)
    count = 0
    while x + down <= height:
        if run < width:
            if lines[x][run] == '#':
                count += 1
            x += down
            run += right
        else:
            new_line = lines[x]*(run - width + 2)
            if new_line[run] == '#':
                count += 1
            x += down
            run += right
    return count
    
with open('day_03.txt') as f:
    with open('day_03.txt') as f:
    lst = [x.strip('\n') for x in f.readlines()]
    print(f'Part 1: {count_tree(lst,1,3)}')
    print(f'Part 2: {count_tree(lst,1,1)*count_tree(lst,1,3)*count_tree(lst,1,5)*count_tree(lst,1,7)*count_tree(lst,2,1)}')
