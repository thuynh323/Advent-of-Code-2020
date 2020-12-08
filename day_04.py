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
class Passport:
    def __init__(self, passport):
        self.passport = passport
        
    def birthyear(self):
        byr_val = re.findall(r'(?<=byr:)\d+', self.passport)
        if byr_val:
            if 1920 <= int(byr_val[0]) <= 2002:
                return int(byr_val[0])
            else:
                return 'invalid'
        else:
            return 'invalid'
            
    def issueyear(self):
        iyr_val = re.findall(r'(?<=iyr:)\d+', self.passport)
        if iyr_val:
            if 2010 <= int(iyr_val[0]) <= 2020:
                return int(iyr_val[0])
            else:
                return 'invalid'
        else:
            return 'invalid'
            
    def expyear(self):
        eyr_val = re.findall(r'(?<=eyr:)\d+', self.passport)
        if eyr_val:
            if 2020 <= int(eyr_val[0]) <= 2030:
                return int(eyr_val[0])
            else:
                return 'invalid'
        else:
            return 'invalid'
            
    def height(self):
        hgt_val = re.findall(r'(\d+cm|\d+in)', self.passport)
        if hgt_val:
            hgt_num = int(re.search(r'^\d+', hgt_val[0]).group())
            hgt_uni = re.search(r'\D+$', hgt_val[0]).group()
            if (hgt_uni == 'cm' and 150 <= hgt_num <= 193) or \
               (hgt_uni == 'in' and 59 <= hgt_num <= 76):
                return hgt_num, hgt_uni
            else:
                return 'invalid'
        else:
            return 'invalid'
            
    def haircolor(self):
        hcl_val = re.findall(r'(?<=hcl:)#[a-f0-9]+', self.passport)
        if hcl_val:
            if len(hcl_val[0]) == 7:
                return hcl_val[0]
            else:
                return 'invalid'
        else:
            return 'invalid'
            
    def eyecolor(self):
        ecl_val = re.findall(r'(?<=ecl:)(amb|blu|brn|gry|grn|hzl|oth)', self.passport)
        if ecl_val:
            return ecl_val[0]
        else:
            return 'invalid'
            
    def passportid(self):
        pid_val = re.findall(r'(?<=pid:)[0-9]+', self.passport)
        if pid_val:
            if len(pid_val[0]) == 9:
                return pid_val[0]
            else:
                return 'invalid'
        else:
            return 'invalid'          

def valid_2(lines):
    count = 0
    for l in lines:
        byr = Passport(l).birthyear()
        iyr = Passport(l).issueyear()
        eyr = Passport(l).expyear()
        hgt = Passport(l).height()
        hcl = Passport(l).haircolor()
        ecl = Passport(l).eyecolor()
        pid = Passport(l).passportid()
        cond_list = [byr, iyr, eyr, hgt, hcl, ecl, pid]
        if 'invalid' not in cond_list:
            count += 1
    return count
with open('day_04.txt') as f:
    lst = f.read().split('\n\n')
    print(f'Number of valid passports from the strict system: {valid_2(lst)}')
