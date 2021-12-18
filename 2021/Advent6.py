import sys
import time
import math

timerLanternFishs = []
fishesGeneratedByStartDay = {}
_NUM_INITIAL_LANTERN_FISH = 0
_INIT_DAYS_NEW_FISH = 8
_DAYS_GENERATE_NEW_BY_FISH = 6


def generateLanternFishes(startDay, lastDay, currentTimer):
    global fishesGeneratedByStartDay

    if (startDay + currentTimer) in fishesGeneratedByStartDay.keys():
        return fishesGeneratedByStartDay[startDay + currentTimer]

    if (startDay > lastDay):
        return -1
    if ((startDay + currentTimer) >= lastDay):
        return 0

    countFishesGenerateUntilEndDay = int(math.floor((lastDay - startDay - currentTimer)/(_DAYS_GENERATE_NEW_BY_FISH + 1))) + 1
    
    countFishesIterativeGenerated = 0
    for i in range(countFishesGenerateUntilEndDay):
        fishStartDay = startDay + currentTimer + i*(_DAYS_GENERATE_NEW_BY_FISH + 1) + 1
        countFishesIterativeGenerated = countFishesIterativeGenerated + generateLanternFishes(fishStartDay, lastDay, _INIT_DAYS_NEW_FISH)

    fishesGeneratedByStartDay[startDay + currentTimer] = countFishesGenerateUntilEndDay + countFishesIterativeGenerated

    return countFishesGenerateUntilEndDay + countFishesIterativeGenerated


def countLanternFishesByDays(days):
    global fishesGeneratedByStartDay
    countFishes = len(timerLanternFishs)
    fishesGeneratedByStartDay = {}

    for timerLanternFish in timerLanternFishs:
        fishesIterative = generateLanternFishes(0, days, timerLanternFish)
        countFishes = countFishes + fishesIterative

    return countFishes

def main(days):
    return countLanternFishesByDays(days)

def readFile():
    global _NUM_INITIAL_LANTERN_FISH
    global timerLanternFishs

    with open("Advent6.txt", "r") as f:
        for strLine in f:
            strLine = strLine.replace('\r', '').replace('\n', '')
            listLanternFishs = strLine.split(',')
            timerLanternFishs = [int(x) for x in listLanternFishs]
        
        _NUM_INITIAL_LANTERN_FISH = len(timerLanternFishs)

readFile()
print('\033[1m' + 'Count of lantern fishs: {0}'.format(_NUM_INITIAL_LANTERN_FISH) + '\033[0m')
if (len(sys.argv) == 2 and sys.argv[1] == '1') or len(sys.argv) == 1:
    # First Exercise
    print('\033[91m\033[1m' + 'First Exercise' + '\033[0m')
    start_time = time.time()
    result1 = main(80)
    print('\033[92m' + '\t - Result: {0}. Time: {1}s'.format(result1, time.time() - start_time) + '\033[0m')
    
if (len(sys.argv) == 2 and sys.argv[1] == '2') or len(sys.argv) == 1:
    # Second Exercise
    print('\033[91m\033[1m' + 'Second Exercise' + '\033[0m')
    start_time = time.time()
    result2 = main(256)
    print('\033[92m' + '\t - Result: {0}. Time: {1}s'.format(result2, time.time() - start_time) + '\033[0m')