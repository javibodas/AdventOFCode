import sys
import time

chitonsRiskLevelMap = []
_NUM_CHITONS_ROWS = 0
_NUM_CHITONS_COLUMNS = 0
queueDistances = []

def getMinNodeFromQueue():
    global queueDistances

    sortedQueue = sorted(queueDistances, key=lambda x: x['distance'])
    minNode = sortedQueue.pop(0)
    queueDistances = sortedQueue

    return minNode['pos']


# Exercise 1
def dijkstraAlgorithm():
    global queueDistances
    distances = [[sys.maxsize for i in range(_NUM_CHITONS_COLUMNS)] for j in range(_NUM_CHITONS_ROWS)]
    visited = [[False for i in range(_NUM_CHITONS_COLUMNS)] for j in range(_NUM_CHITONS_ROWS)]
    distances[0][0] = 0

    currentNode = (0,0)
    queueDistances.append({'pos' : currentNode, 'distance': 0})
    while len(queueDistances) > 0:
        directionsToCalculate = []
        currentX = currentNode[1]
        currentY = currentNode[0]

        if currentX + 1 < _NUM_CHITONS_COLUMNS and not visited[currentY][currentX + 1]:
            directionsToCalculate.append((0, 1))
        if currentY + 1 < _NUM_CHITONS_ROWS and not visited[currentY + 1][currentX]:
             directionsToCalculate.append((1, 0))
        if currentX - 1 > 0 and not visited[currentY][currentX - 1]:
            directionsToCalculate.append((0, -1))
        if currentY - 1 > 0 and not visited[currentY - 1][currentX - 1]:
            directionsToCalculate.append((-1, 0))
        
        for direction in directionsToCalculate:
            nextY = currentY + direction[0]
            nextX = currentX + direction[1]
            estimateDistance = (distances[currentY][currentX] + chitonsRiskLevelMap[nextY][nextX])
            if distances[nextY][nextX] > estimateDistance:
                queueDistances.append({'pos' : (nextY, nextX), 'distance': estimateDistance})
                distances[nextY][nextX] = estimateDistance
        
        visited[currentY][currentX] = True
        currentNode = getMinNodeFromQueue()
    
    return distances[_NUM_CHITONS_ROWS - 1][_NUM_CHITONS_COLUMNS - 1]


# Exercise 2
def searchMinPathForBiggerMap():
    global chitonsRiskLevelMap
    global _NUM_CHITONS_COLUMNS
    global _NUM_CHITONS_ROWS
    global queueDistances
    newchitonsMap = [[0 for i in range(_NUM_CHITONS_COLUMNS * 5)] for j in range(_NUM_CHITONS_ROWS * 5)]

    for row in range(len(chitonsRiskLevelMap)):
        for column in range(len(chitonsRiskLevelMap[row])):
            newchitonsMap[row][column] = chitonsRiskLevelMap[row][column]
            newchitonsMap[row][column + _NUM_CHITONS_COLUMNS] = chitonsRiskLevelMap[row][column] + 1 if chitonsRiskLevelMap[row][column] + 1 < 10 else 1
            newchitonsMap[row][column + (_NUM_CHITONS_COLUMNS * 2)] = chitonsRiskLevelMap[row][column] + 2 if chitonsRiskLevelMap[row][column] + 2 < 10 else (chitonsRiskLevelMap[row][column] + 2) - 9 
            newchitonsMap[row][column + (_NUM_CHITONS_COLUMNS * 3)] = (chitonsRiskLevelMap[row][column] + 3) if chitonsRiskLevelMap[row][column] + 3 < 10 else (chitonsRiskLevelMap[row][column] + 3) - 9
            newchitonsMap[row][column + (_NUM_CHITONS_COLUMNS * 4)] = (chitonsRiskLevelMap[row][column] + 4) if chitonsRiskLevelMap[row][column] + 4 < 10 else (chitonsRiskLevelMap[row][column] + 4) - 9

    for row in range(_NUM_CHITONS_ROWS):
        for column in range(len(newchitonsMap[row])):
            newchitonsMap[row + _NUM_CHITONS_ROWS][column] = newchitonsMap[row][column] + 1 if newchitonsMap[row][column] + 1 < 10 else 1
            newchitonsMap[row + _NUM_CHITONS_ROWS*2][column] = newchitonsMap[row][column] + 2 if newchitonsMap[row][column] + 2 < 10 else (newchitonsMap[row][column] + 2) - 9
            newchitonsMap[row + _NUM_CHITONS_ROWS*3][column] = newchitonsMap[row][column] + 3 if newchitonsMap[row][column] + 3 < 10 else (newchitonsMap[row][column] + 3) - 9
            newchitonsMap[row + _NUM_CHITONS_ROWS*4][column] = newchitonsMap[row][column] + 4 if newchitonsMap[row][column] + 4 < 10 else (newchitonsMap[row][column] + 4) - 9

    queueDistances = []
    chitonsRiskLevelMap = newchitonsMap
    _NUM_CHITONS_COLUMNS = _NUM_CHITONS_COLUMNS * 5
    _NUM_CHITONS_ROWS = _NUM_CHITONS_ROWS * 5
    return dijkstraAlgorithm()


def main(methodOfCalculation):
    return methodOfCalculation()
    

def readFile():
    global chitonsRiskLevelMap
    global _NUM_CHITONS_ROWS
    global _NUM_CHITONS_COLUMNS

    with open("Advent15.txt", "r") as f:
        for strLine in f:
            strLine = strLine.replace('\r', '').replace('\n', '')
            chitonsRiskLevelMap.append([int(x) for x in list(strLine)])
            _NUM_CHITONS_COLUMNS = len(strLine)
            _NUM_CHITONS_ROWS = _NUM_CHITONS_ROWS + 1


readFile()
print('\033[1m' + 'Chitons map of {0}x{1}'.format(_NUM_CHITONS_COLUMNS, _NUM_CHITONS_ROWS) + '\033[0m')
if (len(sys.argv) == 2 and sys.argv[1] == '1') or len(sys.argv) == 1:
    # First Exercise
    print('\033[91m\033[1m' + 'First Exercise' + '\033[0m')
    start_time = time.time()
    result1 = main(dijkstraAlgorithm)
    print('\033[92m' + '\t - Result: {0}. Time: {1}s'.format(result1, time.time() - start_time) + '\033[0m')
    
if (len(sys.argv) == 2 and sys.argv[1] == '2') or len(sys.argv) == 1:
    # Second Exercise
    print('\033[91m\033[1m' + 'Second Exercise' + '\033[0m')
    start_time = time.time()
    result2 = main(searchMinPathForBiggerMap)
    print('\033[92m' + '\t - Result: {0}. Time: {1}s'.format(result2, time.time() - start_time) + '\033[0m')