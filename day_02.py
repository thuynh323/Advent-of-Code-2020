"""
12/06/2020
Day 2: Password Philosophy
"""

import pandas as pd
df = pd.read_csv('day_02.txt',
                 delim_whitespace=True,
                 header=None,
                 names=['condition', 'character', 'password'])
df['condition_1'] = df['condition'].str.split('-', expand=True)[0].astype(int)
df['condition_2'] = df['condition'].str.split('-', expand=True)[1].astype(int)
df.drop('condition', axis=1, inplace=True)
df['character'] = df['character'].str.strip(':')

#*************************************************************************************************#
# Part 1: Each line gives the password policy and then the password.                              #
# The password policy indicates the lowest and highest number of times a given letter must appear #
# for the password to be valid. How many passwords are valid according to this policies?          #
#*************************************************************************************************#

df['count'] = [x.count(y)
               for x, y in zip(df['password'], df['character'])]
df['valid_1'] = [1 if a <= x <= b else 0
                for a, x, b in zip(df['condition_1'], df['count'], df['condition_2'])]
print(f'Number of valid passwords: {df['valid_1'].sum()}')

#*************************************************************************************************#
# Part 2: Each policy actually describes two positions in the password,                           #
# where 1 means the first character, 2 means the second character, and so on.                     #
# (Be careful; Toboggan Corporate Policies have no concept of "index zero"!)                      #
# Exactly one of these positions must contain the given letter.                                   #
# Other occurrences of the letter are irrelevant for the purposes of policy enforcement.          #
# How many passwords are valid according to the new interpretation of the policies?               #
#*************************************************************************************************#

df['valid_2'] = [1 if (a[b - 1] == x or a[c - 1] == x) and
                      (a[b - 1] != a[c - 1]) else 0
                 for a, b, c, x in zip(df['password'], df['condition_1'],
                                       df['condition_2'], df['character'])]
print(f'Number of valid passwords: {df['valid_2'].sum()}')
