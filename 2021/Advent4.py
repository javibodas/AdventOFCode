import sys
import time

boards = []
bingoNumbers = []
_NUM_BINGO_NUMBERS = 0
_NUM_BOARDS = 0
_NUM_COLUMNS_BOARD = 5
_NUM_ROWS_BOARD = 5

def checkBingo(board):
    bingo = False
    countSeenInColumn = [0] * len(board)

    for boardLine in board:
        countSeenNumbersInLine = 0
        for boardNumberPos in range(len(boardLine)):
            if boardLine[boardNumberPos]['seen']:
                countSeenInColumn[boardNumberPos] = countSeenInColumn[boardNumberPos] + 1
                countSeenNumbersInLine = countSeenNumbersInLine + 1
        
        if countSeenNumbersInLine == _NUM_ROWS_BOARD:
            return True
    
    for seenColumn in countSeenInColumn:
        if seenColumn == _NUM_COLUMNS_BOARD:
            return True

    return False

def sumNumbersNotSeen(board):
    notSeenNumbers = []

    for boardLine in board:
        for boardNumber in boardLine:
            if not boardNumber['seen']:
                notSeenNumbers.append(int(boardNumber['value']))

    return sum(notSeenNumbers)

def resetBoards():
    for board in boards:
        for boardLine in board:
            for boardNumber in boardLine:
                boardNumber['seen'] = False

# First Exercise
def bingoGame():

    lastSeenNumber = 0
    currentPosBingoNumbers = 0
    currentBingoNumbers = bingoNumbers[currentPosBingoNumbers:currentPosBingoNumbers + 5]

    while len(currentBingoNumbers) > 0:
        for currentBingoNumber in currentBingoNumbers:
            for board in boards:
                for boardLine in board:
                    for boardNumber in boardLine:
                        if boardNumber['value'] == currentBingoNumber:
                            lastSeenNumber = int(currentBingoNumber)
                            boardNumber['seen'] = True
                
                if checkBingo(board):
                    return (lastSeenNumber,sumNumbersNotSeen(board))
        
        currentBingoNumbers = bingoNumbers[currentPosBingoNumbers:currentPosBingoNumbers + 5] if (currentPosBingoNumbers + 5) < len(bingoNumbers) else bingoNumbers[currentPosBingoNumbers:]
        currentPosBingoNumbers = currentPosBingoNumbers + 5
    
    return (lastSeenNumber,0)

# Second Exercise
def bingoGameWiseWin():

    lastSeenNumber = 0
    currentPosBingoNumbers = 0
    currentBingoNumbers = bingoNumbers[currentPosBingoNumbers:currentPosBingoNumbers + 5]
    winningBoards = []

    while len(currentBingoNumbers) > 0:
        for currentBingoNumber in currentBingoNumbers:
            for board in boards:
                if board in winningBoards:
                    continue

                for boardLine in board:
                    for boardNumber in boardLine:
                        if boardNumber['value'] == currentBingoNumber:
                            lastSeenNumber = int(currentBingoNumber)
                            boardNumber['seen'] = True
                
                if checkBingo(board):
                    winningBoards.append(board)
                    
                    if len(winningBoards) == _NUM_BOARDS:
                        return (lastSeenNumber,sumNumbersNotSeen(board))
        
        currentBingoNumbers = bingoNumbers[currentPosBingoNumbers:currentPosBingoNumbers + 5] if (currentPosBingoNumbers + 5) < len(bingoNumbers) else bingoNumbers[currentPosBingoNumbers:]
        currentPosBingoNumbers = currentPosBingoNumbers + 5
    
    return (lastSeenNumber,0)

# Main
def calculateScore(bingoGameMethod):
    (lastSeenNumber, sumOfNotSeenNumbers) = bingoGameMethod()
    resetBoards()
    print('\tLastSeenNumber: {0}. SumOfNumbersNotSeen: {1}\n'.format(lastSeenNumber, sumOfNotSeenNumbers))

    return lastSeenNumber * sumOfNotSeenNumbers


def readFile():
    global _NUM_BINGO_NUMBERS
    global _NUM_BOARDS
    global bingoNumbers
    global boards

    with open("Advent4.txt", "r") as f:
        bingoNumbers = f.readline()
        bingoNumbers = bingoNumbers.replace('\n', '').split(',')
        _NUM_BINGO_NUMBERS = len(bingoNumbers)
        
        f.readline()
        boards.append([])
        for strLine in f:
            if strLine == '\n':
                _NUM_BOARDS = _NUM_BOARDS + 1
                boards.append([])
                continue

            strLine = strLine.replace('\r', '').replace('\n', '')
            
            boardValueLine = ' '.join(strLine.split()).split(' ')
            boards[_NUM_BOARDS].append([{'seen': False, 'value': value} for value in boardValueLine])

        _NUM_BOARDS = _NUM_BOARDS + 1

readFile()
print('\033[1m' + 'Count of bingo numbers: {0}'.format(_NUM_BINGO_NUMBERS) + '\033[0m')
print('\033[1m' + 'Num of boards: {0}'.format(_NUM_BOARDS) + '\033[0m')
if (len(sys.argv) == 2 and sys.argv[1] == '1') or len(sys.argv) == 1:
    # First Exercise
    print('\033[91m\033[1m' + 'First Exercise' + '\033[0m')
    start_time = time.time()
    result1 = calculateScore(bingoGame)
    print('\033[92m' + '\t - Result: {0}. Time: {1}s'.format(result1, time.time() - start_time) + '\033[0m')
    
if (len(sys.argv) == 2 and sys.argv[1] == '2') or len(sys.argv) == 1:
    # Second Exercise
    print('\033[91m\033[1m' + 'Second Exercise' + '\033[0m')
    start_time = time.time()
    result2 = calculateScore(bingoGameWiseWin)
    print('\033[92m' + '\t - Result: {0}. Time: {1}s'.format(result2, time.time() - start_time) + '\033[0m')