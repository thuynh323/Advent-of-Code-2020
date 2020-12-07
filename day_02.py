"""
12/06/2020
Day 2: Password Philosophy
"""

#*************************************************************************************************#
# Part 1: Each line gives the password policy and then the password.                              #
# The password policy indicates the lowest and highest number of times a given letter must appear #
# for the password to be valid. How many passwords are valid according to this policies?          #
#*************************************************************************************************#

def valid_1(lines):
    count = 0
    for l in lines:
        condition, character, password = l.split(' ')
        condition_1, condition_2 = map(int, condition.split('-'))
        character = character.strip(':')
        if condition_1 <= password.count(character) <= condition_2:
            count += 1
    return count

#*************************************************************************************************#
# Part 2: Each policy actually describes two positions in the password,                           #
# where 1 means the first character, 2 means the second character, and so on.                     #
# (Be careful; Toboggan Corporate Policies have no concept of "index zero"!)                      #
# Exactly one of these positions must contain the given letter.                                   #
# Other occurrences of the letter are irrelevant for the purposes of policy enforcement.          #
# How many passwords are valid according to the new interpretation of the policies?               #
#*************************************************************************************************#

def valid_2(lines):
    count = 0
    for l in lines:
        condition, character, password = l.split(' ')
        condition_1, condition_2 = map(int, condition.split('-'))
        character = character.strip(':')
        if (password[condition_1 - 1] == character or password[condition_2 - 1] == character) and \
           password[condition_1 - 1] != password[condition_2 - 1]:
            count += 1
    return count

with open('day_02.txt') as f:
    lst = [x.strip('\n') for x in f.readlines()]
    print(f'Number of valid passwords according to policy 1: {valid_1(lst)}')
    print(f'Number of valid passwords according to policy 2: {valid_2(lst)}')
