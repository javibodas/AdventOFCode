import sys
import time

_NUMBER_GROUPS = 0
_NUMBER_PASSENGERS = 0
answersGroups = []
answersGroupsByPerson = []

def countAnswersByGroup():

    global answersGroups

    count = 0
    for answersByGroup in answersGroups:
        count += len(answersByGroup)

    return count

def countSameAnswersByGroup():

    global answersGroupsByPerson

    counter = 0
    for answersOfGroup in answersGroupsByPerson:
        sameAnswersGroup = answersOfGroup[0]
        for answersByPerson in answersOfGroup:
            sameAnswersGroup = list(set(sameAnswersGroup) & set(answersByPerson))

        counter += len(sameAnswersGroup)

    return counter

def readFileAnswersGroups():
    global answersGroups
    global answersGroupsByPerson
    global _NUMBER_GROUPS
    global _NUMBER_PASSENGERS

    currentAnswersGroup = []
    #Exercise 2
    currentAnswersGroupByPerson = []
    f = open("Advent6.txt", "r")

    for strLine in f:
        if not bool(strLine.strip()):
            _NUMBER_GROUPS += 1
            answersGroups.append(currentAnswersGroup)
            currentAnswersGroup = []
            #Exercise 2
            answersGroupsByPerson.append(currentAnswersGroupByPerson)
            currentAnswersGroupByPerson = []
            continue

        _NUMBER_PASSENGERS += 1
        if '\r' in strLine:
            strLine = strLine.replace('\r', '')
        if '\n' in strLine:
           strLine = strLine.replace('\n', '')

        strLine = strLine.lower()
        charactersLine = list(strLine)

        #Exercise 2
        answersPerson = []
        for c in charactersLine:
            if c not in currentAnswersGroup:
                currentAnswersGroup.append(c)
            #Exercise 2
            answersPerson.append(c)

        #Exercise 2
        currentAnswersGroupByPerson.append(answersPerson)

    if len(currentAnswersGroup) > 0:
        _NUMBER_GROUPS += 1
        answersGroups.append(currentAnswersGroup)

readFileAnswersGroups()
print("Number of groups: {0}".format(_NUMBER_GROUPS))
print("Number of passengers: {0}".format(_NUMBER_PASSENGERS))
if (len(sys.argv) == 2 and sys.argv[1] == '1') or len(sys.argv) == 1:
    # First Exercise
    print('First Exercise')
    start_time = time.time()
    result = countAnswersByGroup()
    print("\t Result: {0}. Time: {1}".format(result, time.time() - start_time))
if (len(sys.argv) == 2 and sys.argv[1] == '2') or len(sys.argv) == 1:
    # Second Exercise
    print('Second Exercise')
    start_time = time.time()
    result = countSameAnswersByGroup()
    print("\t Result: {0}. Time: {1}".format(result, time.time() - start_time))