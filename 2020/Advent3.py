import sys
from copy import deepcopy
# FIRST EXERCISE
forest = []
_MOVE_TRAVEL = {'x': 3, 'y': 1}
_MAX_X_FOREST = 0
_MAX_Y_FOREST = 0

# SECOND EXERCISE
_DIFFERENT_MOVES_TRAVEL = [(1,1),(3,1),(5,1),(7,1),(1,2)]


# FIRST EXERCISE
def searchTreesFirstTravel():

    countTrees = 0
    currentPosX = 0
    currentPosY = 0

    while currentPosY < _MAX_Y_FOREST:

        if forest[currentPosY][currentPosX] == '#':
            countTrees += 1

        currentPosY = currentPosY + _MOVE_TRAVEL['y']
        currentPosX = (currentPosX + _MOVE_TRAVEL['x']) % _MAX_X_FOREST

    return countTrees

# SECOND EXERCISE
def searchTreesGivenTravel(currentPosX, currentPosY, moveX, moveY):
    
    if currentPosY >= _MAX_Y_FOREST:
        return 0

    if forest[currentPosY][currentPosX] == '.':
        return 0 + searchTreesGivenTravel(((currentPosX + moveX)  % _MAX_X_FOREST), (currentPosY + moveY), moveX, moveY)

    if forest[currentPosY][currentPosX] == '#':
         return 1 + searchTreesGivenTravel(((currentPosX + moveX)  % _MAX_X_FOREST), (currentPosY + moveY), moveX, moveY)

def searchTreesDifferentTravels():

    multiplicationCountTrees = 1

    for move in _DIFFERENT_MOVES_TRAVEL:
        multiplicationCountTrees = multiplicationCountTrees * searchTreesGivenTravel(0, 0, move[0], move[1])

    return multiplicationCountTrees



def readFileForest():
    global forest 
    global _MAX_Y_FOREST
    global _MAX_X_FOREST

    forest = []
    _MAX_Y_FOREST = 0
    f = open("Advent3.txt", "r")

    for x in f:
        lstChar = list(x)
        
        if '\r' in lstChar:
            lstChar.remove('\r')
        if '\n' in lstChar:
            lstChar.remove('\n')

        _MAX_Y_FOREST += 1
        _MAX_X_FOREST = len(lstChar)
        forest.append(lstChar)

readFileForest()
print("Number of rows in forest: {0}".format(_MAX_Y_FOREST))
print("Number of columns in forest: {0}".format(_MAX_X_FOREST)) 
if (len(sys.argv) == 2 and sys.argv[1] == '1') or len(sys.argv) == 1:
    # First Exercise
    print('First Exercise')
    print("\t - Result: {0}".format(searchTreesFirstTravel()))
    
if (len(sys.argv) == 2 and sys.argv[1] == '2') or len(sys.argv) == 1:
    # Second Exercise
    print('Second Exercise')
    readFileForest()
    print("\t - Result: {0}".format(searchTreesDifferentTravels()))