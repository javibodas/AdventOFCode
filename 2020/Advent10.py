import sys
import time
from copy import deepcopy

_NUM_RATES_CHARGERS = 0
_DEFAULT_OUTPUT_JOLTAGE_ADAPTER = 0
_RATE_JOLTAGE_BUILTIN_ADAPTER = 0
rateOutputJoltageAdapters = []


# FIRST EXERCISE
def getJoltDifferences():

    oneJoltageDifference, threeJoltageDifference, currentPosAdapters = 0, 0, 0
    currentOutputJoltageAdapter = _DEFAULT_OUTPUT_JOLTAGE_ADAPTER

    while currentOutputJoltageAdapter < _RATE_JOLTAGE_BUILTIN_ADAPTER:
        if rateOutputJoltageAdapters[currentPosAdapters] == currentOutputJoltageAdapter + 1:
            oneJoltageDifference += 1
            currentOutputJoltageAdapter = rateOutputJoltageAdapters[currentPosAdapters]
        elif rateOutputJoltageAdapters[currentPosAdapters] == currentOutputJoltageAdapter + 3:
            threeJoltageDifference += 1
            currentOutputJoltageAdapter = rateOutputJoltageAdapters[currentPosAdapters]

        currentPosAdapters += 1

    return oneJoltageDifference * threeJoltageDifference

# SECOND EXERCISE
memoization = {}

def getCountDifferentArrangements(curJoltage=_DEFAULT_OUTPUT_JOLTAGE_ADAPTER, curAttachment=[0]):

    global memoization
    if curJoltage == _RATE_JOLTAGE_BUILTIN_ADAPTER:
        return 1

    if curJoltage in memoization:
        return memoization[curJoltage]

    attachments = 0
    if (curJoltage + 1) in rateOutputJoltageAdapters:
        attachments += getCountDifferentArrangements((curJoltage + 1),curAttachment + [(curJoltage + 1)])
        
    if (curJoltage + 2) in rateOutputJoltageAdapters:
        attachments += getCountDifferentArrangements((curJoltage + 2),curAttachment + [(curJoltage + 2)])
        
    if (curJoltage + 3) in rateOutputJoltageAdapters:
        attachments += getCountDifferentArrangements((curJoltage + 3),curAttachment + [(curJoltage + 3)])

    memoization[curJoltage] = attachments

    return attachments


def readJoltages():
    global _NUM_RATES_CHARGERS
    global _RATE_JOLTAGE_BUILTIN_ADAPTER
    global rateOutputJoltageAdapters
    
    f = open("Advent10.txt", "r")

    for strLine in f:

        # Remove break lines
        if '\r' in strLine:
            strLine = strLine.replace('\r', '')
        if '\n' in strLine:
           strLine = strLine.replace('\n', '')

        value = int(strLine)

        rateOutputJoltageAdapters.append(value)
    
    # Device biltin adapter rate equals to higher rate of chargers + 3
    rateOutputJoltageAdapters.sort()
    _RATE_JOLTAGE_BUILTIN_ADAPTER = rateOutputJoltageAdapters[len(rateOutputJoltageAdapters) - 1] + 3
    rateOutputJoltageAdapters.append(_RATE_JOLTAGE_BUILTIN_ADAPTER)
    _NUM_RATES_CHARGERS = len(rateOutputJoltageAdapters)


readJoltages()
print("Number of joltages: {0}".format(_NUM_RATES_CHARGERS))
print("Joltage Builtint adapter: {0}".format(_RATE_JOLTAGE_BUILTIN_ADAPTER))
if (len(sys.argv) == 2 and sys.argv[1] == '1') or len(sys.argv) == 1:
    # First Exercise
    print('First Exercise')
    start_time = time.time()
    result = getJoltDifferences()
    print("\t - Result: {0}. Time: {1}s".format(result, time.time() - start_time))
    
if (len(sys.argv) == 2 and sys.argv[1] == '2') or len(sys.argv) == 1:
    # Second Exercise
    print('Second Exercise')
    start_time = time.time()
    result = getCountDifferentArrangements()
    print("\t - Result: {0}. Time: {1}s".format(result, time.time() - start_time))