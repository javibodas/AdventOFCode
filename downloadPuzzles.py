import requests
import sys
import os
from datetime import datetime
from dotenv import load_dotenv


URI = 'https://adventofcode.com/{0}/day/{1}/input'
currentYear = datetime.now().year
currentDay = datetime.now().day
beginAdventPuzzlesDay = 1
numAdventPuzzlesDays = 25

load_dotenv()
COOKIE=os.getenv('COOKIE')

def downloadPuzzlesYear(year=currentYear, day=0):

    pathYearFolder = './{0}'.format(year)
    if not os.path.exists(pathYearFolder):
        os.mkdir(pathYearFolder)
        print('Folder {0} created.'.format(year))

    initDay = 0
    endDay = 0
    if day == 0:
        initDay = beginAdventPuzzlesDay
        endDay = numAdventPuzzlesDays
    else:
        initDay = day
        endDay = day
    
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



if len(sys.argv) == 2:
        print("Usage: python3 downloadPuzzles.py -y {0} -d {1}".format(currentYear, currentDay))

elif len(sys.argv) == 3:
    if (sys.argv[1] == '-y'):
        if (sys.argv[2].isdigit() and (int(sys.argv[2]) <= currentYear and int(sys.argv[2]) >= 2015)):
            downloadPuzzlesYear(int(sys.argv[2]))
        else:
            print("The year is not valid. Year must be in ( 2015 - {0} )".format(currentYear))
    elif (sys.argv[1] == '-d'):
        print("It is necessary the param -y".format(currentYear))
        print("Usage: python3 downloadPuzzles.py -y {0} -d {1}".format(currentYear, currentDay))

elif len(sys.argv) == 5:
    if sys.argv[1] == '-y':
        if sys.argv[3] == '-d':
            if ((sys.argv[2].isdigit() and (int(sys.argv[2]) <= currentYear and int(sys.argv[2]) >= 2015)) and
                (sys.argv[4].isdigit() and (int(sys.argv[4]) <= numAdventPuzzlesDays and int(sys.argv[4]) >= beginAdventPuzzlesDay))):
                downloadPuzzlesYear(int(sys.argv[2]), int(sys.argv[4]))
            else:
                print("The year or day is not valid. Year must be in ( 2015 - {0} ). Day must be in ( 1 - 25 )".format(currentYear))
        else:
            print("Usage: python3 downloadPuzzles.py -y {0} -d {1}".format(currentYear, currentDay))
    
    elif sys.argv[3] == '-y':
        if sys.argv[1] == '-d':
            if ((sys.argv[4].isdigit() and (int(sys.argv[4]) <= currentYear and int(sys.argv[4]) >= 2015)) and
                (sys.argv[2].isdigit() and (int(sys.argv[2]) <= numAdventPuzzlesDays and int(sys.argv[2]) >= beginAdventPuzzlesDay))):
                downloadPuzzlesYear(int(sys.argv[4]), int(sys.argv[2]))
            else:
                print("The year or day is not valid. Year must be in ( 2015 - {0} ). Day must be in ( 1 - 25 )".format(currentYear))
        else:
            print("Usage: python3 downloadPuzzles.py -y {0} -d {1}".format(currentYear, currentDay))
    
    else:
        print("Usage: python3 downloadPuzzles.py -y {0} -d {1}".format(currentYear, currentDay))
else:
    print("Downloading puzzless of year {0} ...".format(currentYear))
    downloadPuzzlesYear()

    