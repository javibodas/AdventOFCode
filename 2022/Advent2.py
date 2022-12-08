import sys
import time

# The positions of the shapes are in order from lose to win
# A (Rock) lose with B (Paper), B (Paper) lose with C (Scissors)
# Winner is in (currenPos + 1) % 3
_OPPONENT_SHAPES = ['A', 'B', 'C'] # Rock, Paper, Scissors
_ME_SHAPES = ['X', 'Y', 'Z'] # Rock, Paper, Scissors
_OPPONENT = 0
_ME = 1

_NUM_ROUNDS = 0
rounds = []

# Exercise 2
# The position of the letters X, Y, Z minus 1 show the direction of the desire result
# Lose 0 - 1, prev position, Draw 1 - 1 same position, Win 2 - 1, next position
# The shape score is the position of the shape plus 1
def getScoreByRoundShouldEnd():
    sum = 0

    for round in rounds: 
        positionShapeShouldEnd = (_OPPONENT_SHAPES.index(round[_OPPONENT]) + (_ME_SHAPES.index(round[_ME]) - 1)) % 3
        sum += 3*_ME_SHAPES.index(round[_ME]) + (positionShapeShouldEnd + 1)
    
    return sum

# Exercise 1
# The diference between the position of the opponent shape and our shape show the result of each battle
# 0 (DRAW), 1 (WIN), -1(LOSE), 2(LOSE)
# The shape score is the position of the shape plus 1
def getScoreByStrategyGuide():
    sum = 0

    for round in rounds:
        positionDiff = _ME_SHAPES.index(round[_ME]) - _OPPONENT_SHAPES.index(round[_OPPONENT]) 
        sum += (_ME_SHAPES.index(round[_ME]) + 1) + (3*(1 + positionDiff) % 9)
            
    return sum

def readFile():
    global _NUM_ROUNDS
    global rounds
	
    f = open("Advent2.txt", "r")

    for strLine in f:
        
        # Remove break lines
        if '\r' in strLine:
            strLine = strLine.replace('\r', '')
        if '\n' in strLine:
            strLine = strLine.replace('\n', '')

        rounds.append(strLine.split(' '))

        _NUM_ROUNDS += 1


readFile()
print("Number of rounds: {0}".format(_NUM_ROUNDS))
if (len(sys.argv) == 2 and sys.argv[1] == '1') or len(sys.argv) == 1:
    # First Exercise
    print('First Exercise')
    start_time = time.time()
    result1 = getScoreByStrategyGuide()
    print("\t - Result: {0}. Time: {1}s".format(result1, time.time() - start_time))
    
if (len(sys.argv) == 2 and sys.argv[1] == '2') or len(sys.argv) == 1:
    # Second Exercise
    print('Second Exercise')
    start_time = time.time()
    result2 = getScoreByRoundShouldEnd()
    print("\t - Result: {0}. Time: {1}s".format(result2, time.time() - start_time))