import sys
import time

vents = []
ventsDiagram = []
_NUM_OF_VENTS = 0
_MAX_X_POS_VENT = 0
_MAX_Y_POS_VENT = 0

def calculateDiagram(methodOfCalculation):
    for vent in vents:
        currentPos = (vent['xOrigin'], vent['yOrigin'])
        destPos = (vent['xDest'],  vent['yDest'])
        direction = (1 if (currentPos[0] < destPos[0]) else -1, 1 if (currentPos[1] < destPos[1]) else -1)
        #print('({0},{1}) -> ({2},{3})'.format(currentPos[0], currentPos[1], destPos[0], destPos[1]))
        methodOfCalculation(currentPos[0], currentPos[1], destPos[0], destPos[1], direction[0], direction[1])


def countOverlaps(methodOfCalculation):
    calculateDiagram(methodOfCalculation)

    count = 0
    for rowDiagram in ventsDiagram:
        for i in range(len(rowDiagram)):
            if rowDiagram[i] >= 2:
                count = count + 1
    
    return count

def updateLines(rangeOfPositions, currentXPos, currentYPos, destXPos, destYPos, directionX, directionY):
    global ventsDiagram

    for i in range(rangeOfPositions):
        ventsDiagram[currentYPos + (i * directionY)][currentXPos + (i * directionX)] = ventsDiagram[currentYPos + (i * directionY)][currentXPos + (i * directionX)] + 1

# Exercise 1
def checkHorizontalAndVerticalLines(currentXPos, currentYPos, destXPos, destYPos, directionX, directionY):
    rangeOfPositions = 0
    direction = 0

    if currentXPos == destXPos:
        rangeOfPositions = abs(currentYPos - destYPos) + 1
        directionX = 0
    
    if currentYPos == destYPos:
        rangeOfPositions = abs(currentXPos - destXPos) + 1
        directionY = 0

    updateLines(rangeOfPositions, currentXPos, currentYPos, destXPos, destYPos, directionX, directionY)


# Excercise 2
def checkHorizontalVerticalAndDiagonalLines(currentXPos, currentYPos, destXPos, destYPos, directionX, directionY):
    rangeOfPositions = 0
    direction = 0

    if currentXPos == destXPos:
        rangeOfPositions = abs(currentYPos - destYPos) + 1
        directionX = 0
    
    if currentYPos == destYPos:
        rangeOfPositions = abs(currentXPos - destXPos) + 1
        directionY = 0
    
    if currentXPos != destXPos and currentYPos != destYPos:
        rangeOfPositions = abs(currentXPos - destXPos) + 1

    updateLines(rangeOfPositions, currentXPos, currentYPos, destXPos, destYPos, directionX, directionY)


def main(methodOfCalculation):
    global ventsDiagram

    ventsDiagram = [[0 for i in range(_MAX_X_POS_VENT + 1)] for i in range(_MAX_X_POS_VENT + 1)]
    return countOverlaps(methodOfCalculation)


def readFile():
    global _MAX_X_POS_VENT
    global _MAX_Y_POS_VENT
    global _NUM_OF_VENTS
    global vents

    with open("Advent5.txt", "r") as f:
        for strLine in f:
            strLine = strLine.replace('\r', '').replace('\n', '')
            
            ventDirections = strLine.split(' -> ')
            origin = ventDirections[0].split(',')
            dest = ventDirections[1].split(',')

            currentVent = {'xOrigin': int(origin[0]), 'yOrigin': int(origin[1]), 'xDest': int(dest[0]), 'yDest': int(dest[1])}
            vents.append(currentVent)

            if currentVent['xOrigin'] > _MAX_X_POS_VENT:
                _MAX_X_POS_VENT = currentVent['xOrigin']
            if currentVent['xDest'] > _MAX_X_POS_VENT:
                _MAX_X_POS_VENT = currentVent['xDest']
            if currentVent['yOrigin'] > _MAX_Y_POS_VENT:
                _MAX_Y_POS_VENT = currentVent['yOrigin']
            if currentVent['yDest'] > _MAX_Y_POS_VENT:
                _MAX_Y_POS_VENT = currentVent['yDest']
        
        _NUM_OF_VENTS = len(vents)

readFile()
print('\033[1m' + 'Count of vents: {0}'.format(_NUM_OF_VENTS) + '\033[0m')
print('\033[1m' + 'Diagram of {0}x{1}'.format(_MAX_X_POS_VENT + 1, _MAX_Y_POS_VENT + 1) + '\033[0m')
if (len(sys.argv) == 2 and sys.argv[1] == '1') or len(sys.argv) == 1:
    # First Exercise
    print('\033[91m\033[1m' + 'First Exercise' + '\033[0m')
    start_time = time.time()
    result1 = main(checkHorizontalAndVerticalLines)
    print('\033[92m' + '\t - Result: {0}. Time: {1}s'.format(result1, time.time() - start_time) + '\033[0m')
    
if (len(sys.argv) == 2 and sys.argv[1] == '2') or len(sys.argv) == 1:
    # Second Exercise
    print('\033[91m\033[1m' + 'Second Exercise' + '\033[0m')
    start_time = time.time()
    result2 = main(checkHorizontalVerticalAndDiagonalLines)
    print('\033[92m' + '\t - Result: {0}. Time: {1}s'.format(result2, time.time() - start_time) + '\033[0m')