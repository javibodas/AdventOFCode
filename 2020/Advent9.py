import sys
import time

_NUM_SERIES = 0
series = []
_NUMBER_PREAMBLE_SERIES = 25

# Exercise 1
def findIncorrectNumber():
    global _NUMBER_PREAMBLE_SERIES
    global series


    posChecked = _NUMBER_PREAMBLE_SERIES
    endSearch = False

    while posChecked < _NUM_SERIES and not endSearch:
        preambleWindow = series[posChecked - _NUMBER_PREAMBLE_SERIES : posChecked]

        posCheckedIsSumOfNumInPreamble = False
        for i in range(0,_NUMBER_PREAMBLE_SERIES):
            if(preambleWindow[i] > 0 and 
                (series[posChecked] - preambleWindow[i]) > 0 and
                (preambleWindow[i] != series[posChecked] - preambleWindow[i]) and
                (series[posChecked] - preambleWindow[i]) in preambleWindow):
                    posCheckedIsSumOfNumInPreamble = True
                    break

        if not posCheckedIsSumOfNumInPreamble:
            endSearch = True
        else:
            posChecked += 1

    return (posChecked, series[posChecked])

# Exercise 2
def findEncryptionWeakness():
    global series

    ( posIncorrectNumber, incorrectNumber ) = findIncorrectNumber()

    initPosWindow = 0
    endPosWindow = posIncorrectNumber
    foundedRange = False
    rangeSeriesSum = []
    
    while not foundedRange:
        rangeSeriesSum = series[ initPosWindow : endPosWindow ]

        sumSeries = sum(rangeSeriesSum)
        if(sumSeries == incorrectNumber):
            foundedRange = True
        elif(sumSeries > incorrectNumber):
            endPosWindow -= 1
        elif(sumSeries < incorrectNumber and endPosWindow < posIncorrectNumber):
            initPosWindow += 1
            endPosWindow += 1
        elif(sumSeries < incorrectNumber):
            initPosWindow += 1

    rangeSeriesSum.sort()

    return rangeSeriesSum[0] + rangeSeriesSum[len(rangeSeriesSum) - 1]

def readPortOutput():
    global _NUM_SERIES
    global series
    
    f = open("Advent9.txt", "r")

    for strLine in f:

        # Remove break lines
        if '\r' in strLine:
            strLine = strLine.replace('\r', '')
        if '\n' in strLine:
           strLine = strLine.replace('\n', '')

        value = int(strLine)

        series.append(value)
        _NUM_SERIES += 1





readPortOutput()
print("Number of series: {0}".format(_NUM_SERIES))
if (len(sys.argv) == 2 and sys.argv[1] == '1') or len(sys.argv) == 1:
    # First Exercise
    print('First Exercise')
    start_time = time.time()
    result1 = findIncorrectNumber()
    print("\t - Result: {0}. Time: {1}s".format(result1, time.time() - start_time))
    
if (len(sys.argv) == 2 and sys.argv[1] == '2') or len(sys.argv) == 1:
    # Second Exercise
    print('Second Exercise')
    start_time = time.time()
    result2 = findEncryptionWeakness()
    print("\t - Result: {0}. Time: {1}s".format(result2, time.time() - start_time))