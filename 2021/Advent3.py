import sys
import time

diagnostics = []
_NUM_DIAGNOSTICS = 0

def calculateGreaterAndFewerBitInPos(listBits, pos):
    sumBitsInPos = 0

    for bits in listBits:
        lstCharBits = list(bits)
        sumBitsInPos = sumBitsInPos +  int(lstCharBits[pos])

    if sumBitsInPos >= (len(listBits)/2):
        return {'greater' : '1', 'fewer': '0'}
    
    return {'greater' : '0', 'fewer': '1'}

def calculateGreaterAndFewerOcurrencesBits(listBits):
    greaterBits = []
    fewerBits = []

    for i in range(len(listBits[0])):
        greaterAndFewerBitByPos = calculateGreaterAndFewerBitInPos(listBits, i)

        greaterBits.append(greaterAndFewerBitByPos['greater'])
        fewerBits.append(greaterAndFewerBitByPos['fewer'])
    
    return {'greaterBits' : greaterBits, 'fewerBits' : fewerBits}

# Exercise 1
def calculateConsumptionPower():
    result = calculateGreaterAndFewerOcurrencesBits(diagnostics)
    gammaRate = int("".join(result['greaterBits']), 2)
    epsilonRate = int("".join(result['fewerBits']), 2)
    
    return gammaRate * epsilonRate

# Exercise 2
def bitsWithGreaterAndFewerFirstPosBit():
    numbersWithGreaterBit = []
    numbersWithFewerBit = []

    result = calculateGreaterAndFewerBitInPos(diagnostics, 0)
    greaterBitFirstPos = result['greater']

    for diagnostic in diagnostics:
        if diagnostic[0] == greaterBitFirstPos:
            numbersWithGreaterBit.append(list(diagnostic))
        else:
            numbersWithFewerBit.append(list(diagnostic))

    return (numbersWithGreaterBit, numbersWithFewerBit)

def calculateLifeSupportRating():
    (numbersWithGreaterBit, numbersWithFewerBit) = bitsWithGreaterAndFewerFirstPosBit()

    bitCurrentPos = 1
    while len(numbersWithGreaterBit) > 1:
        numbersToRemove = []
        result = calculateGreaterAndFewerBitInPos(numbersWithGreaterBit, bitCurrentPos)
        greaterBitCurrentPos = result['greater']

        for numberWithGreaterBit in numbersWithGreaterBit:
            if numberWithGreaterBit[bitCurrentPos] != greaterBitCurrentPos:
                numbersToRemove.append(numberWithGreaterBit)
        
        for numberToRemove in numbersToRemove:
            numbersWithGreaterBit.remove(numberToRemove)

        bitCurrentPos += 1
    
    bitCurrentPos = 1
    while len(numbersWithFewerBit) > 1:
        numbersToRemove = []
        result = calculateGreaterAndFewerBitInPos(numbersWithFewerBit, bitCurrentPos)
        fewerBitCurrentPos = result['fewer']

        for numberWithFewerBit in numbersWithFewerBit:
            if (numberWithFewerBit[bitCurrentPos] != fewerBitCurrentPos):
                numbersToRemove.append(numberWithFewerBit)
        
        for numberToRemove in numbersToRemove:
            numbersWithFewerBit.remove(numberToRemove)

        bitCurrentPos += 1

    oxygenGeneratorRate = int("".join(numbersWithGreaterBit[0]),2)
    coScrubberRate = int("".join(numbersWithFewerBit[0]), 2)

    return oxygenGeneratorRate * coScrubberRate

def readFile():
    global _NUM_DIAGNOSTICS
    global diagnostics
	
    f = open("Advent3.txt", "r")

    for strLine in f:
        
        # Remove break lines
        if '\r' in strLine:
            strLine = strLine.replace('\r', '')
        if '\n' in strLine:
            strLine = strLine.replace('\n', '')

        diagnostics.append(strLine)
        _NUM_DIAGNOSTICS += 1


readFile()
print("Number of diagnostics: {0}".format(_NUM_DIAGNOSTICS))
if (len(sys.argv) == 2 and sys.argv[1] == '1') or len(sys.argv) == 1:
    # First Exercise
    print('First Exercise')
    start_time = time.time()
    result1 = calculateConsumptionPower()
    print("\t - Result: {0}. Time: {1}s".format(result1, time.time() - start_time))
    
if (len(sys.argv) == 2 and sys.argv[1] == '2') or len(sys.argv) == 1:
    # Second Exercise
    print('Second Exercise')
    start_time = time.time()
    result2 = calculateLifeSupportRating()
    print("\t - Result: {0}. Time: {1}s".format(result2, time.time() - start_time))