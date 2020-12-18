import sys
import time

rulesFields = []
nearbyTickets = []
myTicketData = []
_NUMBER_OF_NEARBY_TICKETS = 0
# SECOND EXERCISE
validTickets = []


# SECOND EXERCISE
def fieldPosSameForAllValidTickets(rule, posValue):

    sameInAllValidTickets = True
    for validTicket in validTickets[1:]:
        if (validTicket[posValue] not in range(rule['first'][0],rule['first'][1] + 1) 
            and validTicket[posValue] not in range(rule['second'][0],rule['second'][1] + 1)):
            sameInAllValidTickets = False

    return sameInAllValidTickets

def checkPosFieldFromValidTicket(field, validTicket):

    pos = 0
    posValue = 0
    validFieldsFounded = []

    while posValue < len(validTicket):
        value, posRule = validTicket[posValue], 0
        validFieldFounded = False
        while not validFieldFounded and posRule < len(rulesFields):
            fieldRule = rulesFields[posRule].keys()[0]
            rule = rulesFields[posRule][fieldRule]
            if ((value in range(rule['first'][0],rule['first'][1] + 1) or value in range(rule['second'][0],rule['second'][1] + 1)) 
                and fieldRule not in validFieldsFounded
                and fieldPosSameForAllValidTickets(rule, posValue)):
                validFieldsFounded.append(fieldRule)
                validFieldFounded = True
                if fieldRule == field:
                    pos = posValue
            posRule += 1
        posValue += 1
    
    return pos

def getValueMyTicketByField(field):
    value = 1
    for rule in rulesFields:
        if rule.keys()[0].startswith(field):
            t = myTicketData[checkPosFieldFromValidTicket(rule.keys()[0], validTickets[0])]
            value *= t
    return value

# FIRST EXERCISE
def checkValidTicketsNearby():

    global validTickets
    notValidValueTickets = []
    for nearTicket in nearbyTickets:

        posValue, notExistInvalidValue = 0, True
        while notExistInvalidValue and posValue < len(nearTicket):

            value, posField, validField = nearTicket[posValue], 0, False
            while not validField and posField < len(rulesFields):
                rule = rulesFields[posField][rulesFields[posField].keys()[0]]
                if (value in range(rule['first'][0],rule['first'][1] + 1) or value in range(rule['second'][0],rule['second'][1] + 1)):
                    validField = True
                posField += 1

            if not validField:
                notExistInvalidValue = False
                notValidValueTickets.append(value)

            posValue += 1

        if notExistInvalidValue:
            validTickets.append(nearTicket)

    #print("\t Valid tickets {0}".format(validTickets))
    return sum(notValidValueTickets)

def readDocumentTickets():

    global rulesFields
    global nearbyTickets
    global myTicket
    global _NUMBER_OF_NEARBY_TICKETS

    f = open("Advent16.txt", "r")

    isMyTicket = False
    for strLine in f:
        if not bool(strLine.strip()):
            continue

        strLine = strLine.replace('\r', '')
        strLine = strLine.replace('\n', '')

        
        if ':' in strLine:
            if strLine.startswith('your ticket'):
                isMyTicket = True
            elif strLine.startswith('nearby tickets'):
                isMyTicket = False
            else:
                [ fieldName, rules ] = strLine.split(': ')
                [ firstRule, secondRule ] = rules.split(' or ')
                rulesFields.append({fieldName:{'first': (int(firstRule[0:firstRule.index('-')]),int(firstRule[firstRule.index('-') + 1:len(firstRule)])),
                                         'second': (int(secondRule[0:secondRule.index('-')]),int(secondRule[secondRule.index('-') + 1:len(secondRule)]))}})

        elif ',' in strLine:
            if isMyTicket:
                fieldValues = strLine.split(',')
                for fieldV in fieldValues:
                    myTicketData.append(int(fieldV))
            else:
                fieldValues = strLine.split(',')
                newTicketFieldValues = []
                for fieldV in fieldValues:
                    newTicketFieldValues.append(int(fieldV))
                nearbyTickets.append(newTicketFieldValues)
            

    
    _NUMBER_OF_NEARBY_TICKETS = len(nearbyTickets)


readDocumentTickets()
print('Count of numbers displayed {0}'.format(_NUMBER_OF_NEARBY_TICKETS))
if (len(sys.argv) == 2 and sys.argv[1] == '1') or len(sys.argv) == 1:
    # First Exercise
    print('First Exercise')
    start_time = time.time()
    result = checkValidTicketsNearby()
    print("\t - Result: {0}. Time: {1}s".format(result, time.time() - start_time))

if (len(sys.argv) == 2 and sys.argv[1] == '2') or len(sys.argv) == 1:
    # Second Exercise
    print('Second Exercise')
    start_time = time.time()
    result = getValueMyTicketByField('departure')
    print("\t - Result: {0}. Time: {1}s".format(result, time.time() - start_time))