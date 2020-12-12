boardPasess = []
seatIDs = []
_AIRPLANE_ROWS = 127
_AIRPLANE_COLUMNS = 7


def getSeatID(row, column):
    return ((row * 8) + column)

def findFreeIDSeat(beginEndRow):

    counterRow = beginEndRow[0]
    foundFreeSeatInRow = False
    rowFounded = []
    while counterRow <= beginEndRow[1] and not foundFreeSeatInRow:
        listActRow = [passFilter for passFilter in boardPasess if passFilter['row'] == counterRow]
        foundFreeSeatInRow = len(listActRow) != _AIRPLANE_COLUMNS + 1
        rowFounded = listActRow
        counterRow = counterRow + 1

    if foundFreeSeatInRow:
        freeRow = rowFounded[0]['row']
        freeColumn = 0

        for i in range(_AIRPLANE_COLUMNS):
            columnExist = [passFilter for passFilter in rowFounded if passFilter['column'] == i]
            if len(columnExist) == 0:
                freeColumn = i
                break

        return getSeatID(freeRow, freeColumn)
    else:
        return 1

def getBeginEndRow():
    print('Begin and end row: ',boardPasess[0]['row'], boardPasess[len(boardPasess) - 1]['row'])
    return (boardPasess[0]['row'] + 1, boardPasess[len(boardPasess) - 1]['row'] - 1)

def orderPassesByRow():
    global boardPasess

    boardPasess = sorted(boardPasess, key=lambda k: k['row'])

def getHighestSeatID():
    global seatIDs

    seatIDs.sort(reverse=True)
    return seatIDs[0]

def foundRowColumnSeatsAirplane():
    global boardPasess

    for boardPass in boardPasess:
        boardCode = boardPass['boardCodePass']

        actRow = (0,_AIRPLANE_ROWS)
        actColumn = (0, _AIRPLANE_COLUMNS)
        for ch in list(boardCode):
            lastRow = actRow[1] + 1
            countRows = lastRow - actRow[0]
            midCountRows = countRows/2

            lastColumn = actColumn[1] + 1
            countColumns = lastColumn - actColumn[0]
            midCountColumns = countColumns/2

            if ch == 'F':
                actRow = (actRow[0], actRow[1] - midCountRows)
            elif ch == 'B':
                actRow = (actRow[0] + midCountRows, actRow[1])
            elif ch == 'R':
                actColumn = (actColumn[0] + midCountColumns, actColumn[1])
            elif ch == 'L':
                actColumn = (actColumn[0], actColumn[1] - midCountColumns)

        if actRow[0] == actRow[1]:
            boardPass['row'] = actRow[0]
        else:
            print('NO FINAL ROW',boardCode, actRow)

        if actColumn[0] == actColumn[1]:
            boardPass['column'] = actColumn[0]
        else:
            print('NO FINAL COLUMN',boardCode, actColumn)

        boardPass['seatID'] = getSeatID(boardPass['row'], boardPass['column'])
        seatIDs.append(boardPass['seatID'])

    #print(boardPasess)    


def readBoardingPasses():
    global boardPasess

    boardPasess = []
    f = open("Advent5.txt", "r")

    for strLine in f:
        if '\r' in strLine:
            strLine = strLine.replace('\r', '')
        if '\n' in strLine:
            strLine = strLine.replace('\n', '')

        boardPasess.append({'boardCodePass': strLine, 'row': 0, 'column': 0, 'seatID' : 0})
    
    #print(boardPasess)


readBoardingPasses()
# FIRST EXERCISE
foundRowColumnSeatsAirplane()
print(getHighestSeatID())
# SECOND EXERCISE
orderPassesByRow()
print(findFreeIDSeat(getBeginEndRow()))