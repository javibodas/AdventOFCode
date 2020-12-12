import sys
import time
from copy import deepcopy

_NUM_RATES_CHARGERS = 0
_POSSIBLE_LESS_INPUT_JOLTAGE = [1 ,2 ,3]
_DEFAULT_OUTPUT_JOLTAGE_ADAPTER = 0
_RATE_JOLTAGE_BUILTIN_ADAPTER = 0
rateOutputJoltageAdapters = []


# FIRST EXERCISE
def getJoltDifferences():

    oneJoltageDifference = 0
    threeJoltageDifference = 0
    currentOutputJoltageAdapter = _DEFAULT_OUTPUT_JOLTAGE_ADAPTER
    currentPosAdapters = 0

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
differentAttachments = []
countDifferentAttachments = 0
""" class TreeNode:
    def __init__(self, value):
        self.joltage1 = None
        self.joltage2 = None
        self.joltage3 = None
        self.value = value
    
    def PrintTree(self):
        print(self.value)
        if self.joltage1:
            self.joltage1.PrintTree()
        if self.joltage2:
            self.joltage2.PrintTree()
        if self.joltage3:
            self.joltage3.PrintTree()

parentNode = TreeNode(0) """
def createDifferentAttachments(curJoltage, curAttachment):

    global differentAttachments
    global countDifferentAttachments

    if curJoltage == _RATE_JOLTAGE_BUILTIN_ADAPTER:
        #print(curAttachment)
        #differentAttachments.append(curAttachment)
        countDifferentAttachments += 1
        return

    if (curJoltage + 1) in rateOutputJoltageAdapters:
        #newAttachment1 = deepcopy(curAttachment)
        #newAttachment1.append(curJoltage + 1)
        #createDifferentAttachments(newAttachment1[len(newAttachment1) - 1],newAttachment1)
        createDifferentAttachments((curJoltage + 1),curAttachment)
        
    if (curJoltage + 2) in rateOutputJoltageAdapters:
        #newAttachment2 = deepcopy(curAttachment)
        #newAttachment2.append(curJoltage + 2)
        #createDifferentAttachments(newAttachment2[len(newAttachment2) - 1],newAttachment2)
        createDifferentAttachments((curJoltage + 2),curAttachment)
        
    if (curJoltage + 3) in rateOutputJoltageAdapters:
        #newAttachment3 = deepcopy(curAttachment)
        #newAttachment3.append(curJoltage + 3)
        #createDifferentAttachments(newAttachment3[len(newAttachment3) - 1],newAttachment3)
        createDifferentAttachments((curJoltage + 3),curAttachment)

    return



def getCountDifferentArrangements():
    global countDifferentAttachments
    createDifferentAttachments(_DEFAULT_OUTPUT_JOLTAGE_ADAPTER, [0])
    #return len(differentAttachments)
    return countDifferentAttachments


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
        _NUM_RATES_CHARGERS += 1
    
    # Device biltin adapter rate equals to higher rate of chargers + 3
    rateOutputJoltageAdapters.sort()
    _RATE_JOLTAGE_BUILTIN_ADAPTER = rateOutputJoltageAdapters[_NUM_RATES_CHARGERS - 1] + 3
    rateOutputJoltageAdapters.append(_RATE_JOLTAGE_BUILTIN_ADAPTER)
    _NUM_RATES_CHARGERS += 1


readJoltages()
print("Number of joltages: {0}".format(_NUM_RATES_CHARGERS))
print("Joltage Builtint adapter: {0}".format(_RATE_JOLTAGE_BUILTIN_ADAPTER))
sys.setrecursionlimit(10000)
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