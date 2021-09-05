import requests
import sys
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

COMMON_USAGE_SCRIPT = 'Usage: python3 downloadPuzzles.py -y {0} -d {1}'
COOKIE = os.getenv('COOKIE')
MIN_YEAR_PUZZLES = 2015
MIN_DAY_PUZZLES = 1
MAX_DAY_PUZZLES = 25
URI = 'https://adventofcode.com/{0}/day/{1}/input'
YEAR_OPTION = '-y'
DAY_OPTION = '-d'

currentYear = datetime.now().year
currentDay = datetime.now().day

def downloadPuzzlesYear(year=currentYear, day=0):

    pathYearFolder = './{0}'.format(year)
    if not os.path.exists(pathYearFolder):
        os.mkdir(pathYearFolder)
        print('Folder {0} created.'.format(year))

    initDay = day
    endDay = day

    if day == 0:
        initDay = MIN_DAY_PUZZLES
        endDay = MAX_DAY_PUZZLES
    
    for i in range(initDay, endDay + 1):

        #Download content puzzle
        URL = URI.format(year, i)
        headers = {'cookie': COOKIE}
        r = requests.get(URL, headers=headers)

        # Check response
        if r.status_code == 404:
            print("Puzzle of day {0} doesnt exist yet.".format(i))
            break
        elif r.status_code != requests.codes.ok:
            print("An error ocurred when download puzzle of day {0}".format(i))
            print(r.status_code)
            continue
            
        puzzleContent = r.text
        print('Puzzle of day {0} in {1} downloaded.'.format(i, year))

        # Write puzzle in file
        pathPuzzle = '{0}/Advent{1}.txt'.format(pathYearFolder, i)
        f = open(pathPuzzle, 'w')
        f.write(puzzleContent)
        f.close()

def isValidYear(year):
    return (year.isdigit() and (int(year) <= currentYear and int(year) >= MIN_YEAR_PUZZLES))

def isValidDay(day):
    return (day.isdigit() and (int(day) <= MAX_DAY_PUZZLES and int(day) >= MIN_DAY_PUZZLES))

def main():
    if len(sys.argv) == 2:
        print(COMMON_USAGE_SCRIPT.format(currentYear, currentDay))
        return

    if len(sys.argv) != 3 and len(sys.argv) != 5:
        print("Downloading puzzless of year {0} ...".format(currentYear))
        downloadPuzzlesYear()
        return


    if len(sys.argv) == 3:
        if (sys.argv[1] != DAY_OPTION and sys.argv[1] != YEAR_OPTION):
            print(COMMON_USAGE_SCRIPT.format(currentYear, currentDay))
            return

        if (sys.argv[1] == DAY_OPTION):
            print("It is necessary the year option (-y {0})".format(currentYear))
            return

        if (sys.argv[1] == YEAR_OPTION):
            if not isValidYear(sys.argv[2]):
                print("The year is not valid. Year must be in ( 2015 - {0} )".format(currentYear))
                return

            downloadPuzzlesYear(int(sys.argv[2]))

    if len(sys.argv) == 5:
        if (not (sys.argv[1] == DAY_OPTION and sys.argv[3] == YEAR_OPTION) and not (sys.argv[1] == YEAR_OPTION or sys.argv[3] == DAY_OPTION)):
            print(COMMON_USAGE_SCRIPT.format(currentYear, currentDay))
            return

        if sys.argv[1] == YEAR_OPTION and sys.argv[3] == DAY_OPTION:
            if (not isValidYear(sys.argv[2]) or not isValidDay(sys.argv[4])):
                print("The year or day is not valid. Year must be in ( 2015 - {0} ). Day must be in ( 1 - 25 )".format(currentYear))
                return
            
            downloadPuzzlesYear(int(sys.argv[2]), int(sys.argv[4]))
        
        if sys.argv[1] == DAY_OPTION and sys.argv[3] == YEAR_OPTION:
            if (not isValidYear(sys.argv[4]) or not isValidDay(sys.argv[2])):
                print("The year or day is not valid. Year must be in ( 2015 - {0} ). Day must be in ( 1 - 25 )".format(currentYear))
                return
            
            downloadPuzzlesYear(int(sys.argv[4]), int(sys.argv[2]))

main()

    