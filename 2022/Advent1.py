import sys
import time


def finfMaxThreeCaloriesElves():
    return elveCaloriesSum[0] + elveCaloriesSum[1] + elveCaloriesSum[2]

def findMaxCaloriesElves():
    return elveCaloriesSum[0]

def readFile():
    global _NUM_ELVES
    global elveCaloriesSum
    _NUM_ELVES = 0
    elveCaloriesSum = []
	
    elveCalories = 0
    f = open("Advent1.txt", "r")
    for strLine in f:
        # Remove break lines
        if '\r' in strLine:
            strLine = strLine.replace('\r', '')
        if '\n' in strLine:
            strLine = strLine.replace('\n', '')
        if strLine == '':
            _NUM_ELVES += 1
            elveCaloriesSum.append(elveCalories)
            elveCalories = 0
            continue

        elveCalories += int(strLine)
    
    _NUM_ELVES += 1
    elveCaloriesSum.append(elveCalories)
    elveCaloriesSum.sort(reverse=True)


readFile()
print("Number of elves: {0}".format(_NUM_ELVES))
if (len(sys.argv) == 2 and sys.argv[1] == '1') or len(sys.argv) == 1:
    # First Exercise
    print('First Exercise')
    start_time = time.time()
    result1 = findMaxCaloriesElves()
    print("\t - Result: {0}. Time: {1}s".format(result1, time.time() - start_time))
    
if (len(sys.argv) == 2 and sys.argv[1] == '2') or len(sys.argv) == 1:
    # Second Exercise
    print('Second Exercise')
    start_time = time.time()
    result2 = finfMaxThreeCaloriesElves()
    print("\t - Result: {0}. Time: {1}s".format(result2, time.time() - start_time))