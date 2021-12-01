import sys
import time

depths = []
_NUM_DEPTHS = 0

# Exercise 1
def findTimesDepthIncrease():
	counterIncreased = 0
	posToCheck = _NUM_DEPTHS - 1

	while posToCheck > 0:
		if depths[posToCheck] > depths[posToCheck - 1]:
			counterIncreased += 1
		
		posToCheck -= 1
	
	return counterIncreased


# Exercise 1
def sumGroupOfThreeDepthsFromPos(pos):
    return sum(depths[pos - 2:pos + 1])

def findTimesDepthIncreaseWithThreeDepths():
    counterIncreased = 0
    posToCheck = _NUM_DEPTHS - 1
    
    while posToCheck > 3:
        if sumGroupOfThreeDepthsFromPos(posToCheck) > sumGroupOfThreeDepthsFromPos(posToCheck - 1):
            counterIncreased += 1
            
        posToCheck -= 1
        
    return counterIncreased
    


def readPortOutput():
    global _NUM_DEPTHS
    global depths
	
    f = open("Advent1.txt", "r")

    for strLine in f:
        
        # Remove break lines
        if '\r' in strLine:
            strLine = strLine.replace('\r', '')
        if '\n' in strLine:
            strLine = strLine.replace('\n', '')

        value = int(strLine)
        depths.append(value)
        _NUM_DEPTHS += 1


readPortOutput()
print("Number of depths: {0}".format(_NUM_DEPTHS))
if (len(sys.argv) == 2 and sys.argv[1] == '1') or len(sys.argv) == 1:
    # First Exercise
    print('First Exercise')
    start_time = time.time()
    result1 = findTimesDepthIncrease()
    print("\t - Result: {0}. Time: {1}s".format(result1, time.time() - start_time))
    
if (len(sys.argv) == 2 and sys.argv[1] == '2') or len(sys.argv) == 1:
    # Second Exercise
    print('Second Exercise')
    start_time = time.time()
    result2 = findTimesDepthIncreaseWithThreeDepths()
    print("\t - Result: {0}. Time: {1}s".format(result2, time.time() - start_time))