"""
12/08/2020
Day 4: Passport Processing
"""

#*************************************************************************************************#
# Part 1: Count the number of valid passports - those that have all required fields.              #
# Treat cid as optional. In your batch file, how many passports are valid?                        #
#*************************************************************************************************#
def valid_1(lines):
    count = 0
    for l in lines:
        byr = int('byr:' in l)
        iyr = int('iyr:' in l)
        eyr = int('eyr:' in l)
        hgt = int('hgt:' in l)
        hcl = int('hcl:' in l)
        ecl = int('ecl:' in l)
        pid = int('pid:' in l)
        cid = int('cid:' in l)
        cond_list = [byr, iyr, eyr, hgt, hcl, ecl, pid, cid]
        if sum(cond_list) == 8 or (sum(cond_list) == 7 and cid == 0):
                count += 1
    return count
 
with open('day_04.txt') as f:
    lst = f.read().split('\n\n')
    print(f'Number of valid passports according to the naive system: {valid_1(lst)}')   
   
#*************************************************************************************************#
# Part 2: You can continue to ignore the cid field, but each other field has strict rules about   #
# what values are valid for automatic validation:                                                 #
#   byr (Birth Year) - four digits; at least 1920 and at most 2002.                               #
#   iyr (Issue Year) - four digits; at least 2010 and at most 2020.                               #
#   eyr (Expiration Year) - four digits; at least 2020 and at most 2030.                          #
#   hgt (Height) - a number followed by either cm or in:                                          #
#       If cm, the number must be at least 150 and at most 193.                                   #
#       If in, the number must be at least 59 and at most 76.                                     #
#   hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.                         #
#   ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.                                #
#   pid (Passport ID) - a nine-digit number, including leading zeroes.                            #
#   cid (Country ID) - ignored, missing or not.                                                   #
#*************************************************************************************************#

import re
def valid_2(lines):
    count = 0
    for l in lines:
        byr = re.findall(r'(?<=byr:)\d+', l)
        iyr = re.findall(r'(?<=iyr:)\d+', l)
        eyr = re.findall(r'(?<=eyr:)\d+', l)
        hgt = re.findall(r'(\d+cm|\d+in)', l)
        hcl = re.findall(r'(?<=hcl:)#[a-f0-9]+', l)
        ecl = re.findall(r'(?<=ecl:)(amb|blu|brn|gry|grn|hzl|oth)', l)
        pid = re.findall(r'(?<=pid:)[0-9]+', l)
        if byr and 1920 <= int(byr[0]) <= 2002: byr = int(byr[0])
        else: continue
        
        if iyr and 2010 <= int(iyr[0]) <= 2020: iyr = int(iyr[0])
        else: continue
        
        if eyr and 2020 <= int(eyr[0]) <= 2030: eyr = int(eyr[0])
        else: continue
            
        if hgt:
            hgt_num = int(re.search(r'^\d+', hgt[0]).group())
            hgt_uni = re.search(r'\D+$', hgt[0]).group()
            if (hgt_uni == 'cm' and 150 <= hgt_num <= 193) or \
               (hgt_uni == 'in' and 59 <= hgt_num <= 76):
                hgt = (hgt_num, hgt_uni)
            else: continue
        else: continue
            
        if hcl and len(hcl[0]) == 7: hcl = hcl[0]
        else: continue
        
        if ecl: ecl = ecl[0]
        else: continue
            
        if pid and len(pid[0]) == 9: pid = pid[0]
        else: continue  

        count += 1
    return count

with open('day_04.txt') as f:
    lst = f.read().split('\n\n')
    print(f'Number of valid passports from the strict system: {valid_2(lst)}')
