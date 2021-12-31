import sys
import time

crabPositions = []
_NUM_HORIZONTAL_POSITIONS = 0

# Exercise 2
def fuelByIncrementalSteps(initialPos, endPos):
    steps = abs(initialPos - endPos)

    return int((steps*(steps+1))/2)

# Exercise 1
def fuelBySteps(initialPos, endPos):
    return abs(initialPos - endPos)

def main(methodOfFuelCalculation):
    maxHorizontalPosition = max(crabPositions)
    minHorizontalPosition = min(crabPositions)

    currentStep = maxHorizontalPosition
    minFuel = sys.maxsize
    while currentStep > minHorizontalPosition:
        currentFuel = 0
        for crabPos in crabPositions:
            currentFuel = currentFuel + methodOfFuelCalculation(crabPos,currentStep)
        
        if currentFuel < minFuel:
            minFuel = currentFuel
        
        currentStep = currentStep - 1

    return minFuel

def readFile():
    global _NUM_HORIZONTAL_POSITIONS
    global crabPositions

    with open("Advent7.txt", "r") as f:
        for strLine in f:
            strLine = strLine.replace('\r', '').replace('\n', '')
            crabPositions = [int(x) for x in strLine.split(',')]
        
        _NUM_HORIZONTAL_POSITIONS = len(crabPositions)

readFile()
print('\033[1m' + 'Count of horizontal positions: {0}'.format(_NUM_HORIZONTAL_POSITIONS) + '\033[0m')
if (len(sys.argv) == 2 and sys.argv[1] == '1') or len(sys.argv) == 1:
    # First Exercise
    print('\033[91m\033[1m' + 'First Exercise' + '\033[0m')
    start_time = time.time()
    result1 = main(fuelBySteps)
    print('\033[92m' + '\t - Result: {0}. Time: {1}s'.format(result1, time.time() - start_time) + '\033[0m')
    
if (len(sys.argv) == 2 and sys.argv[1] == '2') or len(sys.argv) == 1:
    # Second Exercise
    print('\033[91m\033[1m' + 'Second Exercise' + '\033[0m')
    start_time = time.time()
    result2 = main(fuelByIncrementalSteps)
    print('\033[92m' + '\t - Result: {0}. Time: {1}s'.format(result2, time.time() - start_time) + '\033[0m')