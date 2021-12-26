import sys
import time

polymerTemplate = ''
pairsInsertions = {}


def substractMaxAndMinNumElements(iterativeCountNums):
    lIterative = iterativeCountNums

    for char in polymerTemplate:
        if char in lIterative:
            lIterative[char] = lIterative[char] + 1
        else:
            lIterative[char] = 1
    
    print(lIterative)
    
    sortedElements = sorted(lIterative.items(), key=lambda x: x[1])
    return sortedElements[len(sortedElements) - 1][1] - sortedElements[0][1]

memoization = {}
def iterativeGeneratorSubstrings(currentTemplate, iteration):
    localCountElementsMap = {}

    if (currentTemplate + str(iteration)) in memoization:
        return memoization[currentTemplate + str(iteration)]
    
    if iteration == 0:
        return localCountElementsMap

    for i in range(len(currentTemplate) - 1):
        insertedStr = pairsInsertions[currentTemplate[i] + currentTemplate[i+1]]
        
        if insertedStr in localCountElementsMap: localCountElementsMap[insertedStr] = localCountElementsMap[insertedStr] + 1
        else: localCountElementsMap[insertedStr] = 1

        iterativeCountElements = iterativeGeneratorSubstrings(currentTemplate[i] + insertedStr + currentTemplate[i + 1], iteration - 1)

        for k in iterativeCountElements:
            if k in localCountElementsMap: localCountElementsMap[k] = localCountElementsMap[k] + iterativeCountElements[k]
            else: localCountElementsMap[k] = iterativeCountElements[k]


    memoization[currentTemplate + str(iteration)] = localCountElementsMap
    return localCountElementsMap


def main1(count):
    return substractMaxAndMinNumElements(iterativeGeneratorSubstrings(polymerTemplate, count))

def readFile():
    global polymerTemplate
    global pairsInsertions

    with open("Advent14.txt", "r") as f:
        
        strLine = f.readline().replace('\r', '').replace('\n', '')
        polymerTemplate = strLine
        f.readline()

        for strLine in f:
            strLine = strLine.replace('\r', '').replace('\n', '')
            mapValues = strLine.split(' -> ')
            pairsInsertions[mapValues[0]] = mapValues[1]

readFile()
if (len(sys.argv) == 2 and sys.argv[1] == '1') or len(sys.argv) == 1:
    # First Exercise
    print('\033[91m\033[1m' + 'First Exercise' + '\033[0m')
    start_time = time.time()
    result1 = main1(10)
    print('\033[92m' + '\t - Result: {0}. Time: {1}s'.format(result1, time.time() - start_time) + '\033[0m')
    
if (len(sys.argv) == 2 and sys.argv[1] == '2') or len(sys.argv) == 1:
    # Second Exercise
    print('\033[91m\033[1m' + 'Second Exercise' + '\033[0m')
    start_time = time.time()
    result2 = main1(40)
    print('\033[92m' + '\t - Result: {0}. Time: {1}s'.format(result2, time.time() - start_time) + '\033[0m')