import sys
import time

commands = []
_NUM_COMMANDS = 0
_START_POSITION = 0
_COMMAND_POSITION = 0
_UNITS_POSITION = 1

# Exercise 1
def increasePosMethod(command, units, positionValues):
    horizontal = positionValues['horizontal'] if ('horizontal' in positionValues) else _START_POSITION
    depth = positionValues['depth'] if ('depth' in positionValues) else _START_POSITION

    if command == 'forward':
        horizontal += units
    elif command == 'down':
        depth += units
    elif command == 'up':
        depth -= units

    return {'horizontal': horizontal, 'depth': depth }


# Exercise 2
def increasePosMethodWithAim(command, units, positionValues):
    horizontal = positionValues['horizontal'] if ('horizontal' in positionValues) else _START_POSITION
    depth = positionValues['depth'] if ('depth' in positionValues) else _START_POSITION
    aim = positionValues['aim'] if ('aim' in positionValues) else _START_POSITION

    if command == 'forward':
        horizontal += units
        depth += aim * units
    elif command == 'down':
        aim += units
    elif command == 'up':
        aim -= units

    return {'horizontal': horizontal, 'depth': depth, 'aim': aim}

# Main    
def multiplyHorizontalPositionAndDepth(methodOfCalculation):
    positionValues = {}

    for command in commands:
        positionValues = methodOfCalculation(command[_COMMAND_POSITION], command[_UNITS_POSITION], positionValues)
        
    return positionValues['horizontal'] * positionValues['depth']
    


def readFile():
    global _NUM_COMMANDS
    global commands
	
    f = open("Advent2.txt", "r")

    for strLine in f:
        
        # Remove break lines
        if '\r' in strLine:
            strLine = strLine.replace('\r', '')
        if '\n' in strLine:
            strLine = strLine.replace('\n', '')

        listDataLine = strLine.split(' ')
        command = listDataLine[_COMMAND_POSITION]
        units = int(listDataLine[_UNITS_POSITION])
        commands.append((command, units))
        _NUM_COMMANDS += 1


readFile()
print("Number of depths: {0}".format(_NUM_COMMANDS))
if (len(sys.argv) == 2 and sys.argv[1] == '1') or len(sys.argv) == 1:
    # First Exercise
    print('First Exercise')
    start_time = time.time()
    result1 = multiplyHorizontalPositionAndDepth(increasePosMethod)
    print("\t - Result: {0}. Time: {1}s".format(result1, time.time() - start_time))
    
if (len(sys.argv) == 2 and sys.argv[1] == '2') or len(sys.argv) == 1:
    # Second Exercise
    print('Second Exercise')
    start_time = time.time()
    result2 = multiplyHorizontalPositionAndDepth(increasePosMethodWithAim)
    print("\t - Result: {0}. Time: {1}s".format(result2, time.time() - start_time))