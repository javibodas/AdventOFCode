import sys
import time

_NUM_SECTION_PAIRS = 0
sectionPairs = []


# Exercise 2
def getCountSectionOverlapWithOtherPair():
    count = 0

    for sectionPair in sectionPairs:
        firstSectionBeginRangeOverlap = sectionPair[1][0] <= sectionPair[0][0] <= sectionPair[1][1]
        firstSectionEndRangeOverlap = sectionPair[1][0] <= sectionPair[0][1] <= sectionPair[1][1]
        secondSectionBeginRangeOverlap = sectionPair[0][0] <= sectionPair[1][0] <= sectionPair[0][1]
        secondSectionEndRangeOverlap = sectionPair[0][0] <= sectionPair[1][1] <= sectionPair[0][1]
        firstSectionOverlap = firstSectionBeginRangeOverlap or firstSectionEndRangeOverlap
        secondSectionOverlap = secondSectionBeginRangeOverlap or secondSectionEndRangeOverlap

        if firstSectionOverlap or secondSectionOverlap:
            count += 1

    return count

# Exercise 1
def getCountSectionFullyContainedByOtherPair():
    count = 0

    for sectionPair in sectionPairs:
        firstSectionBeginRangeContained = sectionPair[1][0] <= sectionPair[0][0] <= sectionPair[1][1]
        firstSectionEndRangeContained = sectionPair[1][0] <= sectionPair[0][1] <= sectionPair[1][1]
        secondSectionBeginRangeContained = sectionPair[0][0] <= sectionPair[1][0] <= sectionPair[0][1]
        secondSectionEndRangeContained = sectionPair[0][0] <= sectionPair[1][1] <= sectionPair[0][1]
        firstSectionContained = firstSectionBeginRangeContained and firstSectionEndRangeContained
        secondSectionContained = secondSectionBeginRangeContained and secondSectionEndRangeContained

        if firstSectionContained or secondSectionContained:
            count += 1

    return count

def readFile():
    global _NUM_SECTION_PAIRS
    global sectionPairs
	
    f = open("Advent4.txt", "r")

    for strLine in f:
        
        # Remove break lines
        if '\r' in strLine:
            strLine = strLine.replace('\r', '')
        if '\n' in strLine:
            strLine = strLine.replace('\n', '')

        sectionPair = strLine.split(',')
        sectionPairs.append([(int(sectionPair[0].split('-')[0]), int(sectionPair[0].split('-')[1])),(int(sectionPair[1].split('-')[0]),int(sectionPair[1].split('-')[1]))])
        
        _NUM_SECTION_PAIRS += 1


readFile()
print("Number of pairs: {0}".format(_NUM_SECTION_PAIRS))
if (len(sys.argv) == 2 and sys.argv[1] == '1') or len(sys.argv) == 1:
    # First Exercise
    print('First Exercise')
    start_time = time.time()
    result1 = getCountSectionFullyContainedByOtherPair()
    print("\t - Result: {0}. Time: {1}s".format(result1, time.time() - start_time))
    
if (len(sys.argv) == 2 and sys.argv[1] == '2') or len(sys.argv) == 1:
    # Second Exercise
    print('Second Exercise')
    start_time = time.time()
    result2 = getCountSectionOverlapWithOtherPair()
    print("\t - Result: {0}. Time: {1}s".format(result2, time.time() - start_time))