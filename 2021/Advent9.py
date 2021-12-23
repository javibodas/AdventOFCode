import sys
import time

heightsMap = []
lowPoints = []
_NUM_ROWS_MAP = 0
_NUM_COLUMS_MAP = 0


def getAdjacentsPositionsLessThanValue(posX, posY, value):
    posXToCheck = []
    posYToCheck = []
    adjacentPositionsLessThanValue = []

    if posX > 0:
        posXToCheck.append(-1)
    if posX < (_NUM_COLUMS_MAP - 1):
        posXToCheck.append(1)
    if posY > 0:
        posYToCheck.append(-1)
    if posY < (_NUM_ROWS_MAP - 1):
        posYToCheck.append(1)

    [adjacentPositionsLessThanValue.append((posY + yOffset, posX)) for yOffset in posYToCheck if value >= heightsMap[posY + yOffset][posX]]
    [adjacentPositionsLessThanValue.append((posY, posX + xOffset)) for xOffset in posXToCheck if value >= heightsMap[posY][posX + xOffset]]

    return adjacentPositionsLessThanValue

# Exercise 2
def getAdjacentsPositionsLessThan9(posX, posY, curPositions):
    adjacentPositionsLessThan = getAdjacentsPositionsLessThanValue(posX, posY, 8)
    if len(adjacentPositionsLessThan) == 0:
        return []
    
    iterativePositions = []
    for adjacentPosition in adjacentPositionsLessThan:
        if adjacentPosition not in curPositions and adjacentPosition not in iterativePositions:
            iterativePositions.append(adjacentPosition)
            iterativePositions = iterativePositions + getAdjacentsPositionsLessThan9(adjacentPosition[1], adjacentPosition[0], curPositions + iterativePositions)

    return iterativePositions

def main2():
    result = []
    for lowPoint in lowPoints:
        adjacentPositionsLessThan9 = len(getAdjacentsPositionsLessThan9(lowPoint[1], lowPoint[0], []))
        result.append(adjacentPositionsLessThan9)

    result.sort()

    return result[len(result) - 1] * result[len(result) - 2] * result[len(result) - 3]

# Exercise 1
def main1():
    global lowPoints
    sumHeights = 0

    for heightsPos in range(len(heightsMap)):
        for heightPos in range(len(heightsMap[heightsPos])):
            if len(getAdjacentsPositionsLessThanValue(heightPos, heightsPos, heightsMap[heightsPos][heightPos])) == 0:
                lowPoints.append((heightsPos, heightPos))
                sumHeights = sumHeights + 1 + heightsMap[heightsPos][heightPos]

    return sumHeights

def readFile():
    global heightsMap
    global _NUM_ROWS_MAP
    global _NUM_COLUMS_MAP

    with open("Advent9.txt", "r") as f:
        for strLine in f:
            strLine = strLine.replace('\r', '').replace('\n', '')
            heightsMap.append([int(x) for x in list(strLine)])
            _NUM_COLUMS_MAP = len(strLine)
            _NUM_ROWS_MAP = _NUM_ROWS_MAP + 1


readFile()
print('\033[1m' + 'Map heights of {0}x{1}'.format(_NUM_ROWS_MAP, _NUM_COLUMS_MAP) + '\033[0m')
if (len(sys.argv) == 2 and sys.argv[1] == '1') or len(sys.argv) == 1:
    # First Exercise
    print('\033[91m\033[1m' + 'First Exercise' + '\033[0m')
    start_time = time.time()
    result1 = main1()
    print('\033[92m' + '\t - Result: {0}. Time: {1}s'.format(result1, time.time() - start_time) + '\033[0m')
    
if (len(sys.argv) == 2 and sys.argv[1] == '2') or len(sys.argv) == 1:
    # Second Exercise
    print('\033[91m\033[1m' + 'Second Exercise' + '\033[0m')
    start_time = time.time()
    result2 = main2()
    print('\033[92m' + '\t - Result: {0}. Time: {1}s'.format(result2, time.time() - start_time) + '\033[0m')