import sys
import time
import math

navigationSubsystem = []
_NUM_LINES_SUBSYSTEM = 0
_OPENING_CHARS = ['(', '[', '{', '<']
_CLOSING_CHARS_MAP = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
    '<' : '>'
}
_ILLEGAL_CHAR_PUNTUATIONS_MAP = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137
}

_INCOMPLETE_CHAR_PUNTUATIONS_MAP = {
    ')' : 1,
    ']' : 2,
    '}' : 3,
    '>' : 4
}

def parseNavigation(navigation):
    stackChars = []
    corruptedChar = ''

    for char in list(navigation):
        if char in _OPENING_CHARS:
            stackChars.append(char)
        else:
            if char == _CLOSING_CHARS_MAP[stackChars[len(stackChars) - 1]]:
                stackChars.pop()
            else:
                corruptedChar = char
                break
    
    return (corruptedChar, stackChars)

# Exercise 2
def calculateScoreIncompleteNavigation(navigation):
    (corruptedChar, stackCharsRemained) = parseNavigation(navigation)
    score = 0

    if corruptedChar == '':
        for charRemained in stackCharsRemained[::-1]:
            score = score*5 + _INCOMPLETE_CHAR_PUNTUATIONS_MAP[_CLOSING_CHARS_MAP[charRemained]]

    return score

def main2():
    results = []
    for navigation in navigationSubsystem:
        result = calculateScoreIncompleteNavigation(navigation)
        if result > 0: results.append(result)
    
    results.sort()
    
    return results[math.floor(len(results)/2)]


# Exercise 1
def calculateScoreError(navigation):
    (corruptedChar, stackCharsRemained) = parseNavigation(navigation)
    score = 0
    
    if corruptedChar != '':
        score = _ILLEGAL_CHAR_PUNTUATIONS_MAP[corruptedChar]

    return score

def main1():
    result = 0
    for navigation in navigationSubsystem:
        result = result + calculateScoreError(navigation)
    
    return result


def readFile():
    global navigationSubsystem
    global _NUM_LINES_SUBSYSTEM

    with open("Advent10.txt", "r") as f:
        for strLine in f:
            strLine = strLine.replace('\r', '').replace('\n', '')
            navigationSubsystem.append(strLine)
            _NUM_LINES_SUBSYSTEM = _NUM_LINES_SUBSYSTEM + 1


readFile()
print('\033[1m' + 'Lines in navigation subsystem: {0}'.format(_NUM_LINES_SUBSYSTEM) + '\033[0m')
if (len(sys.argv) == 2 and sys.argv[1] == '1') or len(sys.argv) == 1:
    # First Exercise
    print('\033[91m\033[1m' + 'First Exercise' + '\033[0m')
    start_time = time.time()
    result1 = main1()
    print('\033[92m' + '\t - Result: {0}. Time: {1}s'.format(result1, time.time() - start_time) + '\033[0m')
    
if (len(sys.argv) == 2 and sys.argv[1] == '2') or len(sys.argv) == 1:
    # Second Exercise
    print('\033[91m\033[1m' + 'Second Exercise' + '\033[0m')
    start_time = time.time()
    result2 = main2()
    print('\033[92m' + '\t - Result: {0}. Time: {1}s'.format(result2, time.time() - start_time) + '\033[0m')