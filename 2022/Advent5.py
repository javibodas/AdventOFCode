import sys
import time

_NUM_REARRANGEMENTS = 0
_NUM_STACKS = 0
cratesStacks = []
rearrangementProcedures = []

def printTopCratesInStacks(stacks):
    result = ['' for i in range(0, _NUM_STACKS)]
    for i in range(0, len(stacks)):
        for j in range(0, len(stacks[i])):
            if i == len(stacks) - 1 and result[j] == '':
                result[j] = stacks[i][j][1:-1]
                continue
            if stacks[i][j] != '[0]' and stacks[i + 1][j] == '[0]':
                result [j] = stacks[i][j][1:-1]

    return ''.join(result)

# Exercise 2
def getCratesOnTopWithMoveInSameOrder():
    localStacks = [i.copy() for i in cratesStacks]

    for rearrangement in rearrangementProcedures:
        elementsToMove = rearrangement[0]
        fromStack = rearrangement[1]
        toStack = rearrangement[2]

        elementsToInsert = []
        # Search and remove crate
        for i in range(0, int(elementsToMove)):
            for j in range(0, len(localStacks)):
                if j == len(localStacks) - 1:
                    elementsToInsert.insert(0, localStacks[j][int(fromStack) - 1])
                    localStacks[j][int(fromStack) - 1] = '[0]'
                    break

                if localStacks[j + 1][int(fromStack) - 1] == '[0]':
                    elementsToInsert.insert(0,localStacks[j][int(fromStack) - 1])
                    localStacks[j][int(fromStack) - 1] = '[0]'
                    break
            
        # Insert crate
        for elementToInsert in elementsToInsert:
            if localStacks[len(localStacks) - 1][int(toStack) - 1] != '[0]':
                localStacks.append(['[0]' for i in range(0, len(localStacks[0]))])
                localStacks[len(localStacks) - 1][int(toStack) - 1] = elementToInsert
                continue

            for j in range(0, len(localStacks)):
                if localStacks[j][int(toStack) - 1] == '[0]':
                    localStacks[j][int(toStack) - 1] = elementToInsert
                    break
    
    return printTopCratesInStacks(localStacks)

# Exercise 1
def getCratesOnTop():
    localStacks = [i.copy() for i in cratesStacks]

    for rearrangement in rearrangementProcedures:
        elementsToMove = rearrangement[0]
        fromStack = rearrangement[1]
        toStack = rearrangement[2]

        for i in range(0, int(elementsToMove)):
            elementToInsert = ''
            # Search and remove crate
            for j in range(0, len(localStacks)):
                if j == len(localStacks) - 1:
                    elementToInsert = localStacks[j][int(fromStack) - 1]
                    localStacks[j][int(fromStack) - 1] = '[0]'
                    break

                if localStacks[j + 1][int(fromStack) - 1] == '[0]':
                    elementToInsert = localStacks[j][int(fromStack) - 1]
                    localStacks[j][int(fromStack) - 1] = '[0]'
                    break
            
            # Insert crate
            if localStacks[len(localStacks) - 1][int(toStack) - 1] != '[0]':
                localStacks.append(['[0]' for i in range(0, len(localStacks[0]))])
                localStacks[len(localStacks) - 1][int(toStack) - 1] = elementToInsert
                continue

            for j in range(0, len(localStacks)):
                if localStacks[j][int(toStack) - 1] == '[0]':
                    localStacks[j][int(toStack) - 1] = elementToInsert
                    break
    
    return printTopCratesInStacks(localStacks)


def readFile():
    global _NUM_REARRANGEMENTS
    global _NUM_STACKS
    global cratesStacks
    global rearrangementProcedures
	
    f = open("Advent5.txt", "r")

    lines = [ strLine.replace('\r', '').replace('\n', '') for strLine in f ]

    separationIdx = lines.index('')
    crates = [cratesLine.replace(']    ', '] [0]').replace('    [', '[0] [').split(' ') for cratesLine in lines[ 0 : separationIdx ]]
    cratesStacks = crates[0:len(crates) - 1]
    cratesStacks.reverse()
    rearrangementProcedures = [rearrangementLine.split(' ')[1::2] for rearrangementLine in lines[ separationIdx + 1 :]]
    
    _NUM_REARRANGEMENTS = len(rearrangementProcedures)
    _NUM_STACKS = len(cratesStacks[0])


readFile()
print("Number of crates: {0}. Number of rearrangements: {1}".format(_NUM_STACKS, _NUM_REARRANGEMENTS))
if (len(sys.argv) == 2 and sys.argv[1] == '1') or len(sys.argv) == 1:
    # First Exercise
    print('First Exercise')
    start_time = time.time()
    result1 = getCratesOnTop()
    print("\t - Result: {0}. Time: {1}s".format(result1, time.time() - start_time))
    
if (len(sys.argv) == 2 and sys.argv[1] == '2') or len(sys.argv) == 1:
    # Second Exercise
    print('Second Exercise')
    start_time = time.time()
    result2 = getCratesOnTopWithMoveInSameOrder()
    print("\t - Result: {0}. Time: {1}s".format(result2, time.time() - start_time))