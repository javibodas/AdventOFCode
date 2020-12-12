import sys
from copy import deepcopy
codeInstructions = []
instructionsVisited = []
_NUM_INSTRUCTIONS = 0

# FIRST EXERCISE
def runBootCode(instructionsCode):
    global instructionsVisited

    # FIRST EXERCISE
    instructionRepeated = False
    currentPosInstruction = 0
    accumulator = 0
    # SECOND EXERCISE
    lastInstructionPassed = False

    while not instructionRepeated and not lastInstructionPassed:
        
        if instructionsVisited[currentPosInstruction]:
            instructionRepeated = True
            continue   

        instructionsVisited[currentPosInstruction] = True
        
        if instructionsCode[currentPosInstruction][0] == 'nop' or instructionsCode[currentPosInstruction][0] == 'acc':
            if instructionsCode[currentPosInstruction][0] == 'acc':
                accumulator += instructionsCode[currentPosInstruction][1]

            currentPosInstruction += 1
        elif instructionsCode[currentPosInstruction][0] == 'jmp':
            currentPosInstruction += instructionsCode[currentPosInstruction][1]

        if currentPosInstruction >= _NUM_INSTRUCTIONS:
            lastInstructionPassed = True

    return (accumulator, lastInstructionPassed)

# SECOND EXERCISE
def getNextJmpNopInstruction(pos, instructions):
    
    for i in range(pos + 1, len(instructions) - 1):
        if(instructions[i][0] == 'jmp'):
            return (i, 'nop')
        elif(instructions[i][0] == 'nop'):
            return (i, 'jmp')

def fixBootCode():
    global codeInstructions
    global instructionsVisited

    codeFixed = False
    accumulator = 0
    currentPosCodeModified = 0
    while not codeFixed:
        fixedInstructions = deepcopy(codeInstructions)

        (currentPosCodeModified, valueInstructionModified ) = getNextJmpNopInstruction(currentPosCodeModified, fixedInstructions)
        fixedInstructions[currentPosCodeModified][0] = valueInstructionModified

        instructionsVisited = [False] * _NUM_INSTRUCTIONS

        (accumulator, codeFixed) = runBootCode(fixedInstructions)

    print("\t - Fixed with line {0} modified to {1}".format(currentPosCodeModified + 1, fixedInstructions[currentPosCodeModified][0]))

    return accumulator

def readBootCode():
    global codeInstructions
    global instructionsVisited
    global _NUM_INSTRUCTIONS
    
    f = open("Advent8.txt", "r")

    for strLine in f:

        # Remove break lines
        if '\r' in strLine:
            strLine = strLine.replace('\r', '')
        if '\n' in strLine:
           strLine = strLine.replace('\n', '')

        lineParams = strLine.split(' ')
        instruction = lineParams[0]
        value = int(lineParams[1])

        codeInstructions.append([instruction, value])
        instructionsVisited.append(False)
        _NUM_INSTRUCTIONS += 1


readBootCode()
print("Number of instructions: {0}".format(_NUM_INSTRUCTIONS))
if (len(sys.argv) == 2 and sys.argv[1] == '1') or len(sys.argv) == 1:
    # First Exercise
    print('First Exercise')
    print("\t - Result: {0}".format(runBootCode(codeInstructions)))
    
if (len(sys.argv) == 2 and sys.argv[1] == '2') or len(sys.argv) == 1:
    # Second Exercise
    print('Second Exercise')
    print("\t - Result: {0}".format(fixBootCode()))
    