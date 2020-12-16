import sys
import time

_NUM_INSTRUCTIONS = 0
_MASK_INSTRUCTION = 'mask'
_MEM_INSTRUCTION = 'mem'
_BITS_MASK = 36
initPortInstructions = []


# EXERCISE 2
# The mask generate address as much as all possibility of floating positions
def applyMaskv2(mask, value):
    newAddresses = []

    bitsValue = format(value, str(_BITS_MASK) + "b").replace(' ','0')
    listMask, listValue = list(mask), list(bitsValue)
    bitsNewAddress = ''
    for i in range(0, _BITS_MASK):
        if listMask[i] == '0':
            bitsNewAddress += listValue[i]
        else:
            bitsNewAddress += listMask[i]

    numberOfFloatingPoints = bitsNewAddress.count('X')
    for i in range(0, 2**numberOfFloatingPoints):
        bitsCurrentChange = format(i, str(numberOfFloatingPoints) + "b").replace(' ','0')
        strCurrentChangeBits = bitsNewAddress
        for b in bitsCurrentChange:
            strCurrentChangeBits = strCurrentChangeBits.replace('X',b, 1)

        newAddresses.append(strCurrentChangeBits)

    for i in range(0, len(newAddresses)):
        newAddresses[i] = int(newAddresses[i], 2)

    return newAddresses


def decoderChipv2():
    result = {}

    currMask = 'X'*36
    for inst in initPortInstructions:
        if _MASK_INSTRUCTION in inst:
            currMask = inst[_MASK_INSTRUCTION]
        elif _MEM_INSTRUCTION in inst:
                newAddresses = applyMaskv2(currMask, inst[_MEM_INSTRUCTION][0])
                for newAddress in newAddresses:
                    result[newAddress] = inst[_MEM_INSTRUCTION][1]

    value = 0
    for r in result:
        value += result[r]

    return value

# EXERCISE 1
def applyMask(mask, value):

    bitsValue = format(value, str(_BITS_MASK) + "b").replace(' ','0')
    listMask, listValue = list(mask), list(bitsValue)
    bitsResult = ''
    for i in range(0, _BITS_MASK):
        if listMask[i] == 'X':
            bitsResult += listValue[i]
        else:
            if int(listValue[i]) == 0:
                bitsResult += listMask[i]
            else:
                bitsResult += str(int(listMask[i]) * int(listValue[i]))

    return int(bitsResult, 2)
    


def decoderChip():
    result = {}

    currMask = 'X'*36
    for inst in initPortInstructions:
        if _MASK_INSTRUCTION in inst:
            currMask = inst[_MASK_INSTRUCTION]
        elif _MEM_INSTRUCTION in inst:
                result[inst[_MEM_INSTRUCTION][0]] = applyMask(currMask, inst[_MEM_INSTRUCTION][1])

    value = 0
    for r in result:
        value += result[r]

    return value


def readInitializationProgram():

    global _NUM_INSTRUCTIONS
    global initPortInstructions

    f = open("Advent14.txt", "r")
    initPortInstructions = []
    _NUM_INSTRUCTIONS = 0

    for strLine in f:
        if not bool(strLine.strip()):
            continue

        strLine = strLine.replace('\r', '')
        strLine = strLine.replace('\n', '')

        if strLine.startswith(_MASK_INSTRUCTION):
            [instruction, value] = strLine.split(' = ')
            initPortInstructions.append({instruction: value})

        elif strLine.startswith(_MEM_INSTRUCTION):
            [memPosStr, value] = strLine.split(' = ')
            memPosStr = memPosStr.replace('[',' ')
            memPosStr = memPosStr.replace(']','')
            [instruction, pos] = memPosStr.split(' ')
            initPortInstructions.append({instruction: (int(pos), int(value))})

    _NUM_INSTRUCTIONS = len(initPortInstructions)


readInitializationProgram()
print('Number of instructions {0}'.format(_NUM_INSTRUCTIONS))
if (len(sys.argv) == 2 and sys.argv[1] == '1') or len(sys.argv) == 1:
    # First Exercise
    print('First Exercise')
    start_time = time.time()
    result = decoderChip()
    print("\t - Result: {0}. Time: {1}s".format(result, time.time() - start_time))

if (len(sys.argv) == 2 and sys.argv[1] == '2') or len(sys.argv) == 1:
    # Second Exercise
    print('Second Exercise')
    start_time = time.time()
    result = decoderChipv2()
    print("\t - Result: {0}. Time: {1}s".format(result, time.time() - start_time))

