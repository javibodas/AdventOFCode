import sys
import time

navitagionInstructions = []
_DIRECTIONS = ['N', 'E', 'S', 'W']
_NUM_INSTRUCTIONS = 0


# SECOND EXERCISE
def navigateNewRules():
    return

# FIRST EXERCISE
def navigate():

    currDirection = [0, 0]
    directionToFace = _DIRECTIONS.index('E')
    for i in range(0, len(navitagionInstructions)):
        if navitagionInstructions[i][0] == 'F':
            if _DIRECTIONS[directionToFace]== 'E':
                currDirection[0] +=  navitagionInstructions[i][1]
            elif _DIRECTIONS[directionToFace] == 'W':
                currDirection[0] -=  navitagionInstructions[i][1]
            elif _DIRECTIONS[directionToFace] == 'S':
                currDirection[1] -=  navitagionInstructions[i][1]
            elif _DIRECTIONS[directionToFace] == 'N':
                currDirection[1] +=  navitagionInstructions[i][1]

        elif navitagionInstructions[i][0] == 'N':
            currDirection[1] += navitagionInstructions[i][1]
        elif navitagionInstructions[i][0] == 'S':
            currDirection[1] -= navitagionInstructions[i][1]
        elif navitagionInstructions[i][0] == 'W':
            currDirection[0] -= navitagionInstructions[i][1]
        elif navitagionInstructions[i][0] == 'E':
            currDirection[0] += navitagionInstructions[i][1]
        elif navitagionInstructions[i][0] == 'R':
            directionToFace = int(directionToFace +  navitagionInstructions[i][1]/90) % len(_DIRECTIONS)
        elif navitagionInstructions[i][0] == 'L':
            if (directionToFace -  navitagionInstructions[i][1]/90) > 0:
                directionToFace = int(directionToFace -  navitagionInstructions[i][1]/90) % len(_DIRECTIONS)
            else:
                directionToFace = int((directionToFace -  navitagionInstructions[i][1]/90) + len(_DIRECTIONS)) % len(_DIRECTIONS)

    return abs(currDirection[0]) + abs(currDirection[1])


def readNavigationInstructions():
    global _NUM_INSTRUCTIONS
    global navitagionInstructions
    
    f = open("Advent12.txt", "r")
    navitagionInstructions = []
    _NUM_INSTRUCTIONS = 0

    for strLine in f:
        # Remove break lines
        if not bool(strLine.strip()):
            continue
        if '\r' in strLine:
            strLine = strLine.replace('\r', '')
        if '\n' in strLine:
           strLine = strLine.replace('\n', '')

        _NUM_INSTRUCTIONS += 1
        direction = strLine[0]
        units = int(strLine[1:])
        navitagionInstructions.append((direction, units))

readNavigationInstructions()
print("Num instructions {0}".format(_NUM_INSTRUCTIONS))
if (len(sys.argv) == 2 and sys.argv[1] == '1') or len(sys.argv) == 1:
    # First Exercise
    print('First Exercise')
    start_time = time.time()
    result = navigate()
    print("\t - Result: {0}. Time: {1}s".format(result, time.time() - start_time))

if (len(sys.argv) == 2 and sys.argv[1] == '2') or len(sys.argv) == 1:
    # Second Exercise
    print('Second Exercise')
    start_time = time.time()
    result = navigateNewRules()
    print("\t - Result: {0}. Time: {1}s".format(result, time.time() - start_time))
