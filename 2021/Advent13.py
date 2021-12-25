import sys
import time

paper = []
dotsPositions = []
foldsInstructions = []
_MAX_NUM_COLUMNS = 0
_MAX_NUM_ROWS = 0


def printPaper(paperToPRINT):
    for row in paperToPRINT:
        print(row)
    print('\n')

def initializePaper():
    global paper

    paper = [['.' for i in range(_MAX_NUM_COLUMNS + 1)] for i in range(_MAX_NUM_ROWS + 1)]
    for dotPosition in dotsPositions:
        paper[dotPosition[1]][dotPosition[0]] = '#'

def countPoints():
    count = 0
    for row in paper:
        for point in row:
            if point == '#': count = count + 1
    
    return count

def markLineToFold(wayFold, line):
    global paper

    if wayFold == 'x':
        for i in range(len(paper)):
            paper[i][line] = '-'
    elif wayFold == 'y':
        for i in range(len(paper[0])):
            paper[line][i] = '-'

def foldWithInstruction(foldsInstruction):
    global paper

    lineToFold = foldsInstruction[1]
    #markLineToFold(foldsInstruction[0], lineToFold)

    paperFolded = []
    if foldsInstruction[0] == 'x':
        for i in range(len(paper)):
            paperFolded.append(['.' for x in range(lineToFold)])
            for j in range(lineToFold):
                paperFolded[i][j] = paper[i][j]
        
        for row in range(len(paper)):
            for column in range(lineToFold + 1, len(paper[row])):
                if (paperFolded[row][abs((column % lineToFold) - lineToFold) % lineToFold] == '.'):
                    paperFolded[row][abs((column % lineToFold) - lineToFold) % lineToFold] = paper[row][column]

    elif foldsInstruction[0] == 'y':
        for i in range(foldsInstruction[1]):
            paperFolded.append(paper[i])
        
        for row in range(lineToFold + 1,len(paper)):
            for column in range(len(paper[row])):
                if (paperFolded[abs((row % lineToFold) - lineToFold) % lineToFold][column] == '.'):
                    paperFolded[abs((row % lineToFold) - lineToFold) % lineToFold][column] = paper[row][column]

    return paperFolded

# Exercise 2
def main2():
    global paper
    initializePaper()

    for foldInstruction in foldsInstructions:
        paper = foldWithInstruction(foldInstruction)
    
    printPaper(paper)
    
    return countPoints()

# Exercise 1
def main1():
    global paper
    initializePaper()
    
    paper = foldWithInstruction(foldsInstructions[0])
    
    return countPoints() 

def readFile():
    global dotsPositions
    global foldsInstructions
    global _MAX_NUM_COLUMNS
    global _MAX_NUM_ROWS

    with open("Advent13.txt", "r") as f:
        for strLine in f:
            strLine = strLine.replace('\r', '').replace('\n', '')
            if strLine == '': break
            
            position = strLine.split(',')
            dotsPositions.append((int(position[0]), int(position[1])))
            
            if int(position[0]) > _MAX_NUM_COLUMNS:
                _MAX_NUM_COLUMNS = int(position[0])
            if int(position[1]) > _MAX_NUM_ROWS:
                _MAX_NUM_ROWS = int(position[1])

        for strLine in f:
            strLine = strLine.replace('\r', '').replace('\n', '').replace('fold along ', '')
            foldsInstruction = strLine.split('=')
            foldsInstructions.append((foldsInstruction[0], int(foldsInstruction[1])))


readFile()
print('\033[1m' + 'Transparent paper of {0}x{1}'.format(_MAX_NUM_COLUMNS, _MAX_NUM_ROWS) + '\033[0m')
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