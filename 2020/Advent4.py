passports = []
numberOfPassports = 0
_REQUIRED_PASSPORT_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] 




def validationYears(byr, iyr, eyr):
    return ((byr.isdigit() and iyr.isdigit() and eyr.isdigit()) and
            (len(byr) == 4 and len(iyr) == 4 and len(eyr) == 4) and
            (int(eyr) > int(iyr) > int(byr)) and
            ((int(eyr) >= 2020) and (2010 <= int(iyr) <= 2020) and (1920 <= int(byr) <= 2002)))

def validationEcl(e):
    return (len(e) == 3) and (e in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl','oth'])

import sys

def validationHgt(e):
    #return (e.endswith('cm') and len(e) == 5) or (e.endswith('in') and len(e) == 4)
    return (e.endswith('cm')) or (e.endswith('in'))

def validationHcl(e):
    listHex = list(e)[1:]
    print(listHex)
    isOk = (e.startswith('#')) and (len(e) == 7)

    if isOk:
        print(e)

    return isOk

def validationPid(e):
    return e.isdigit() and len(e) == 9



def checkFieldsPassports():

    global passports
    global _REQUIRED_PASSPORT_FIELDS

    countValidPassport = 0

    for passport in passports:
        passportKeys = passport.keys()
        check = all(item in passportKeys for item in _REQUIRED_PASSPORT_FIELDS)

        if check:
            #print('OK keys: ', passport['ecl'],validationEcl(passport['ecl']))
            check = (validationYears(passport['byr'],passport['iyr'], passport['eyr']) and validationEcl(passport['ecl']) and validationHgt(passport['hgt'])
                    and validationHcl(passport['hcl']) and validationPid(passport['pid']))
            
            if check:
                countValidPassport = countValidPassport + 1

    return countValidPassport



def readFilePassport():
    global passports
    global numberOfPassports

    passports = []
    currentPassport = {}
    count_blanks = 0
    f = open("Advent4.txt", "r")

    for strLine in f:
        if not bool(strLine.strip()):
            count_blanks += 1
            passports.append(currentPassport)
            currentPassport = {}
            continue

        if '\r' in strLine:
            strLine = strLine.replace('\r', '')
        if '\n' in strLine:
            strLine = strLine.replace('\n', '')

        listDataLine = strLine.split(' ')

        for data in listDataLine:
            keyValue = data.split(':')
            currentPassport[keyValue[0]] = keyValue[1]

    numberOfPassports = len(passports)

readFilePassport()
print("Number of passports: {0}".format(numberOfPassports))
if (len(sys.argv) == 2 and sys.argv[1] == '1') or len(sys.argv) == 1:
    # First Exercise
    print('First Exercise')
    print("\t - Result: {0}".format(checkFieldsPassports()))
    
if (len(sys.argv) == 2 and sys.argv[1] == '2') or len(sys.argv) == 1:
    # Second Exercise
    print('Second Exercise')
    print("\t - Result: {0}".format(fixBootCode()))

