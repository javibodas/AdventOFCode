import sys
import time
from copy import deepcopy

_NUM_SEATS = 0
_NUM_SEAT_ROWS = 0
_NUM_SEAT_COLUMNS = 0
_ADJACENT_POSITIONS = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
_TOLERATE_OCCUPIED_SEATS = [4, 5]
seatsMatrix = []

# SECOND EXERCISE
def findIterativeSeatMove(row, column, move):
    
    if move[0] + column in range(0, _NUM_SEAT_ROWS) and move[1] + row in range(0, _NUM_SEAT_COLUMNS):
        if seatsMatrix[row + move[1]][column + move[0]] == '#':
            return True
        elif seatsMatrix[row + move[1]][column + move[0]] == 'L':
            return False
        else:
            return findIterativeSeatMove(move[1] + row,move[0] + column,move)
    else:
        return False

def getNumSeatsOccupiedSecondRules(tolerateSeatsOccupied):

    global seatsMatrix

    stateChanged = True
    countOccupiedSeats = 0

    while stateChanged:
        newSeatsMatrix = deepcopy(seatsMatrix)
        matrixChanged = False
        countOccupiedSeats = 0

        for currRowSeat in range(0, _NUM_SEAT_ROWS):
            for currColumSeat in range(0, _NUM_SEAT_COLUMNS):

                if seatsMatrix[currRowSeat][currColumSeat] in ['L', '#']:

                    countSeats = 0
                    for movement in _ADJACENT_POSITIONS:
                        if findIterativeSeatMove(currRowSeat, currColumSeat, movement):
                            countSeats += 1

                    if seatsMatrix[currRowSeat][currColumSeat] == 'L' and countSeats == 0:
                        matrixChanged = True
                        newSeatsMatrix[currRowSeat][currColumSeat] = '#'
                    elif newSeatsMatrix[currRowSeat][currColumSeat] == '#' and countSeats >= tolerateSeatsOccupied:
                        matrixChanged = True
                        newSeatsMatrix[currRowSeat][currColumSeat] = 'L'


            countOccupiedSeats += newSeatsMatrix[currRowSeat].count('#')

        seatsMatrix = newSeatsMatrix
        stateChanged = matrixChanged

    return countOccupiedSeats

   

# FIRST EXERCISE
def getNumSeatsOccupiedFirstRules(tolerateSeatsOccupied):

    global seatsMatrix

    stateChanged = True
    countOccupiedSeats = 0

    while stateChanged:
        newSeatsMatrix = deepcopy(seatsMatrix)
        matrixChanged = False
        countOccupiedSeats = 0

        for currRowSeat in range(0, _NUM_SEAT_ROWS):
            for currColumSeat in range(0, _NUM_SEAT_COLUMNS):

                if seatsMatrix[currRowSeat][currColumSeat] in ['L', '#']:

                    countSeats = 0
                    for movement in _ADJACENT_POSITIONS:
                        if  (movement[0] + currColumSeat in range(0, _NUM_SEAT_COLUMNS) 
                            and movement[1] + currRowSeat in range(0, _NUM_SEAT_ROWS) 
                            and seatsMatrix[currRowSeat + movement[1]][currColumSeat + movement[0]] == '#'):
                            countSeats += 1

                    if seatsMatrix[currRowSeat][currColumSeat] == 'L' and countSeats == 0:
                        matrixChanged = True
                        newSeatsMatrix[currRowSeat][currColumSeat] = '#'
                    elif newSeatsMatrix[currRowSeat][currColumSeat] == '#' and countSeats >= tolerateSeatsOccupied:
                        matrixChanged = True
                        newSeatsMatrix[currRowSeat][currColumSeat] = 'L'


            countOccupiedSeats += newSeatsMatrix[currRowSeat].count('#')

        seatsMatrix = newSeatsMatrix
        stateChanged = matrixChanged

    return countOccupiedSeats


def readSeats():
    global _NUM_SEATS
    global _NUM_SEAT_ROWS
    global _NUM_SEAT_COLUMNS
    global seatsMatrix
    
    f = open("Advent11.txt", "r")
    seatsMatrix = []
    _NUM_SEATS = 0
    _NUM_SEAT_ROWS = 0
    _NUM_SEAT_COLUMNS = 0

    for strLine in f:
        # Remove break lines
        if not bool(strLine.strip()):
            continue
        if '\r' in strLine:
            strLine = strLine.replace('\r', '')
        if '\n' in strLine:
           strLine = strLine.replace('\n', '')


        listSeats = list(strLine)
        _NUM_SEAT_ROWS += 1
        _NUM_SEAT_COLUMNS = len(listSeats)
        _NUM_SEATS += len(listSeats)
        seatsMatrix.append(listSeats)



readSeats()
print("Num of seats: {0}".format(_NUM_SEATS))
print("Num of seat rows: {0}".format(_NUM_SEAT_ROWS))
print("Num of seat columns: {0}".format(_NUM_SEAT_COLUMNS))
if (len(sys.argv) == 2 and sys.argv[1] == '1') or len(sys.argv) == 1:
    # First Exercise
    print('First Exercise')
    start_time = time.time()
    result = getNumSeatsOccupiedFirstRules(_TOLERATE_OCCUPIED_SEATS[0])
    print("\t - Result: {0}. Time: {1}s".format(result, time.time() - start_time))
    
if (len(sys.argv) == 2 and sys.argv[1] == '2') or len(sys.argv) == 1:
    # Second Exercise
    print('Second Exercise')
    readSeats()
    start_time = time.time()
    result = getNumSeatsOccupiedSecondRules(_TOLERATE_OCCUPIED_SEATS[1])
    print("\t - Result: {0}. Time: {1}s".format(result, time.time() - start_time))