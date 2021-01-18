"""
12/08/2020
Day 5: Binary Boarding
"""

#*************************************************************************************************#
# Part 1:  The first 7 characters will either be F or B; these specify exactly one of the         #
# 128 rows on the plane (numbered 0 through 127). Each letter tells you which half of a region    #
# the given seat is in. Start with the whole list of rows; the first letter indicates whether     #
# the seat is in the front (0 through 63) or the back (64 through 127). The next letter indicates #
# which half of that region the seat is in, and so on until you're left with exactly one row.     #
#                                                                                                 #
# The last three characters will be either L or R; these specify exactly one of the 8 columns     #
# of seats on the plane (numbered 0 through 7). The same process as above proceeds again,         #
# this time with only three steps. L means to keep the lower half,                                #
# while R means to keep the upper half.                                                           #
#                                                                                                 #
# Every seat also has a unique seat ID: multiply the row by 8, then add the column.               #
# As a sanity check, look through your list of boarding passes. What is the highest seat ID       #
# on a boarding pass?                                                                             #
#*************************************************************************************************#

from statistics import median
def find_seat(lines):
    row = []
    col = []
    for l in lines:
        val1 = list(range(0,128))
        val2 = list(range(0,8))
        for i in range(0,7):
            half1 = len(val1)//2
            if l[i] == 'F':
                del val1[-half1:]
            else:
                del val1[:half1]
        row.append(val1[0])
            
        for j in range(7,10):
            half2 = len(val2)//2
            if l[j] == 'R':
                del val2[:half2]
            else:
                del val2[-half2:]
        col.append(val2[0])
    seat_id = [r*8 + c for r, c in zip(row,col)]
    print(f'The highest seat ID is: {max(seat_id)}')
    
#*************************************************************************************************#
# Part 2:  It's a completely full flight, so your seat should be the only missing boarding pass   #
# in your list. However, there's a catch: some of the seats at the very front and back            #
# of the plane don't exist on this aircraft, so they'll be missing from your list as well.        #
#                                                                                                 #
# Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1                #
# from yours will be in your list. What is the ID of your seat?                                   #
#*************************************************************************************************#

    id_plus = [s + 1 for s in seat_id]
    id_minus = [s - 1 for s in seat_id]
    missing_seat = []
    for s in id_plus:
        if s not in seat_id:
            missing_seat.append(s)
    for s in id_minus:
        if s not in seat_id:
            missing_seat.append(s)
    print(f'The missing seat IDs are: {set(missing_seat)}')
    print(f'My seat ID is: {median(set(missing_seat))}')
    
with open('day_05.txt') as f:
    lst = [x.strip('\n') for x in f.readlines()]
    find_seat(lst)
