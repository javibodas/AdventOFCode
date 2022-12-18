import sys
import time

signalPatternsAndOutputs = []
_NUM_PATTERNS = 0
_NUMBER_NUM_SEGMENTS_MAP = {
    6 : [0, 6, 9],
    5 : [2, 3, 5],
    2 : [1],
    4 : [4],
    3 : [7],
    7 : [8],
}
_NUM_SEGMENTS_POSITIONS = {
    0 : [0, 1, 2, 4, 5, 6],
    1 : [2, 6], 
    2 : [1, 2, 3, 4, 5, 6],
    3 : [1, 2, 3, 5, 6],
    4 : [0, 2, 3, 6],
    5 : [0, 1, 3, 5, 6],
    6 : [0, 1, 3, 4, 5, 6],
    7 : [1, 2, 6],
    8 : [0, 1, 2, 3, 4, 5, 6],
    9 : [0, 1, 2, 3, 5, 6]
}

def getNumbersByLen(length):
    return _NUMBER_NUM_SEGMENTS_MAP[length]

# Exercise 2
def calculatePattern(patterns):
    segmentPattern = {}
    print(patterns)
    patterns.sort(key=len)
    for pattern in patterns:
        numbersByLen = getNumbersByLen(len(pattern))
        if  len(numbersByLen) == 1:
            pattern.sort()
            charsPattern = list(pattern)
            for position in _NUM_SEGMENTS_POSITIONS[numbersByLen[0]]:
                if position not in segmentPattern:
                    segmentPattern[position] = pattern
                else:
                    if len(segmentPattern[position]) > len(pattern):
                        segmentPattern[position] = charsPattern
                    else:
                        for char in charsPattern:
                            if char in segmentPattern[position]:
                                print('Char {0} eliminated from pattern {1} at position {2}'.format(char, pattern, position))
                                charsPattern.remove(char)
                                print(charsPattern)
    
    print(segmentPattern)

    return 0



def getOutputNumber(patterns, outputs):
    return calculatePattern(patterns)

# Exercise 1
def countOcurrencesNumbersWithUniqueNumberOfSegments(patterns, outputs):
    count = 0
    
    for output in outputs:
        numbersByLen = getNumbersByLen(len(output))
        if  len(numbersByLen) == 1:
            count = count + 1 

    return count

def main(methodOfCalculation):
    count = 0

    for signalPatterAndOutput in signalPatternsAndOutputs:
        output = signalPatterAndOutput['output']
        pattern = signalPatterAndOutput['pattern']
        count = count + methodOfCalculation(pattern, output)
    
    return count


def readFile():
    global _NUM_PATTERNS
    global signalPatternsAndOutputs

    with open("Advent8_ex.txt", "r") as f:
        for strLine in f:
            strLine = strLine.replace('\r', '').replace('\n', '')

            [ signalPatterns, outputs ] = strLine.split('|')
            signalPatternsAndOutputs.append({'pattern': signalPatterns[:-1].split(' '), 'output': outputs[1:].split(' ')})

            _NUM_PATTERNS = _NUM_PATTERNS + 1

        #print('Signal Patterns: {0}'.format(signalPatterns))
        #print('Outputs: {0}'.format(outputsPatterns))

readFile()
print('\033[1m' + 'Count of patterns: {0}'.format(_NUM_PATTERNS) + '\033[0m')
if (len(sys.argv) == 2 and sys.argv[1] == '1') or len(sys.argv) == 1:
    # First Exercise
    print('\033[91m\033[1m' + 'First Exercise' + '\033[0m')
    start_time = time.time()
    result1 = main(countOcurrencesNumbersWithUniqueNumberOfSegments)
    print('\033[92m' + '\t - Result: {0}. Time: {1}s'.format(result1, time.time() - start_time) + '\033[0m')
    
if (len(sys.argv) == 2 and sys.argv[1] == '2') or len(sys.argv) == 1:
    # Second Exercise
    print('\033[91m\033[1m' + 'Second Exercise' + '\033[0m')
    start_time = time.time()
    result2 = main(getOutputNumber)
    print('\033[92m' + '\t - Result: {0}. Time: {1}s'.format(result2, time.time() - start_time) + '\033[0m')