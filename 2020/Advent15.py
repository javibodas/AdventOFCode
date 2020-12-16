import sys
import time

numbersDisplayed = []
_NUM_NUMBERS_DISPLAY = 0

def playGame(turns):

    numbersByTurn = {}
    turn = 1
    lastNumberSpoken = '0'

    for numberDisplayed in numbersDisplayed:
        lastNumberSpoken = numberDisplayed
        numbersByTurn[lastNumberSpoken] = {'count': 1, 'lastSpoken': turn}
        turn += 1
    
    while turn <= turns:
        if lastNumberSpoken in numbersByTurn:
            if numbersByTurn[lastNumberSpoken]['count'] == 1:
                lastNumberSpoken = '0'
                numbersByTurn[lastNumberSpoken]['count'] = numbersByTurn[lastNumberSpoken]['count'] + 1
                numbersByTurn[lastNumberSpoken]['earlySpoken'] = numbersByTurn[lastNumberSpoken]['lastSpoken']
                numbersByTurn[lastNumberSpoken]['lastSpoken'] = turn
            elif numbersByTurn[lastNumberSpoken]['count'] > 1:
                lastNumberSpoken = str(numbersByTurn[lastNumberSpoken]['lastSpoken'] - numbersByTurn[lastNumberSpoken]['earlySpoken'])
                if lastNumberSpoken in numbersByTurn:
                    numbersByTurn[lastNumberSpoken]['count'] = numbersByTurn[lastNumberSpoken]['count'] + 1
                    numbersByTurn[lastNumberSpoken]['earlySpoken'] = numbersByTurn[lastNumberSpoken]['lastSpoken']
                    numbersByTurn[lastNumberSpoken]['lastSpoken'] = turn
                else:
                    numbersByTurn[lastNumberSpoken] = {'count': 1, 'lastSpoken': turn}
        else:
            numbersByTurn[lastNumberSpoken] = {'count': 1, 'lastSpoken': turn}

        turn += 1

    return lastNumberSpoken


def readNumbersDisplay():

    global numbersDisplayed
    global _NUM_NUMBERS_DISPLAY

    f = open("Advent15.txt", "r")

    for strLine in f:
        if not bool(strLine.strip()):
            continue

        strLine = strLine.replace('\r', '')
        strLine = strLine.replace('\n', '')

        numbersDisplayed = strLine.split(',')
    
    _NUM_NUMBERS_DISPLAY = len(numbersDisplayed)


readNumbersDisplay()
print('Count of numbers displayed {0}'.format(_NUM_NUMBERS_DISPLAY))
if (len(sys.argv) == 2 and sys.argv[1] == '1') or len(sys.argv) == 1:
    # First Exercise
    print('First Exercise')
    start_time = time.time()
    result = playGame(2020)
    print("\t - Result: {0}. Time: {1}s".format(result, time.time() - start_time))

if (len(sys.argv) == 2 and sys.argv[1] == '2') or len(sys.argv) == 1:
    # Second Exercise
    print('Second Exercise')
    start_time = time.time()
    result = playGame(30000000)
    print("\t - Result: {0}. Time: {1}s".format(result, time.time() - start_time))