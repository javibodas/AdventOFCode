import sys
import time
import string

_NUM_RUCKSACKS = 0
ruckSacks = []
pritoritizes =  string.ascii_lowercase + string.ascii_uppercase

def getPrioritize(item):
    return pritoritizes.index(item) + 1

# Exercise 2
def getSumPrioritiesBageItem():
    sum = 0
    for i in range(0, len(ruckSacks) - 1, 3):
        itemsRepeated = set([item for item in ruckSacks[i] if ruckSacks[i+1].count(item) > 0 and ruckSacks[i+2].count(item) > 0])
        
        for itemRepeated in itemsRepeated:
            sum += getPrioritize(itemRepeated)
    
    return sum

# Exercise 1
def getSumPrioritiesItemTypes():
    sum = 0
    for ruckSack in ruckSacks:
        compartiments = (ruckSack[0:int(len(ruckSack)/2)], ruckSack[int(len(ruckSack)/2):])
        for itemRepeated in set([item for item in compartiments[0] if compartiments[1].count(item) > 0]):
            sum += getPrioritize(itemRepeated)

    return sum

def readFile():
    global _NUM_RUCKSACKS
    global ruckSacks
	
    f = open("Advent3.txt", "r")

    for strLine in f:
        
        # Remove break lines
        if '\r' in strLine:
            strLine = strLine.replace('\r', '')
        if '\n' in strLine:
            strLine = strLine.replace('\n', '')

        ruckSacks.append(strLine)
        _NUM_RUCKSACKS += 1


readFile()
print("Number of rounds: {0}".format(_NUM_RUCKSACKS))
if (len(sys.argv) == 2 and sys.argv[1] == '1') or len(sys.argv) == 1:
    # First Exercise
    print('First Exercise')
    start_time = time.time()
    result1 = getSumPrioritiesItemTypes()
    print("\t - Result: {0}. Time: {1}s".format(result1, time.time() - start_time))
    
if (len(sys.argv) == 2 and sys.argv[1] == '2') or len(sys.argv) == 1:
    # Second Exercise
    print('Second Exercise')
    start_time = time.time()
    result2 = getSumPrioritiesBageItem()
    print("\t - Result: {0}. Time: {1}s".format(result2, time.time() - start_time))