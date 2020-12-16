import sys
import time
import math

_EARLIEST_TIMESTAMP_BUS_COULD_TAKE = 0
_NUMBER_BUSES = 0
buses = []
busIds = []
timeStamps = {}
_ALL_BUS_ID_MULTIPLICATION = 1


# SECOND EXERCISE
def getEarlyTimestampSubsequentBuses(iterationBegin, iterationEnd, firstBus):

    iteration = iterationBegin
    founded = False
    timeStamp = 0
    while not founded and iteration < iterationEnd:

        timeIsSubsequent = True
        timeStamp = iteration * firstBus
        for busID in busIds[1:]:
            busTimeStamp = (iteration + math.ceil(iteration * ((firstBus-busID)/busID))) * busID
            timeIsSubsequent = timeIsSubsequent and (timeStamp + timeStamps[busID]['offset'] == busTimeStamp)

        if not timeIsSubsequent:
            iteration = iteration + 1
        else:
            founded = timeIsSubsequent
            
    return timeStamp


def parallelEarlyTimestampSubsequent():
    iterations = round(_ALL_BUS_ID_MULTIPLICATION/busIds[0])
    return getEarlyTimestampSubsequentBuses(1, iterations, busIds[0])


# FIRST EXERCISE
def getEarliestIDBusMultiplyTimeWait():

    earlyTimeStamp = _EARLIEST_TIMESTAMP_BUS_COULD_TAKE
    earlyBusID = 0

    for busID in busIds:
        currIntBudID = int(busID)
        timeStampBusID = (int(_EARLIEST_TIMESTAMP_BUS_COULD_TAKE / currIntBudID) + 1) * currIntBudID
        timeStampDifference = (timeStampBusID - _EARLIEST_TIMESTAMP_BUS_COULD_TAKE)

        if timeStampDifference < earlyTimeStamp:
            earlyTimeStamp = timeStampDifference
            earlyBusID = currIntBudID
    
    return earlyBusID * earlyTimeStamp



def readBusData():

    global _EARLIEST_TIMESTAMP_BUS_COULD_TAKE
    global _NUMBER_BUSES
    global buses
    global busIds
    global timeStamps
    global _ALL_BUS_ID_MULTIPLICATION


    f = open("Advent13.txt", "r")
    navitagionInstructions = []
    _NUM_INSTRUCTIONS = 0

    for strLine in f:
        if not bool(strLine.strip()):
            continue

        strLine = strLine.replace('\r', '')
        strLine = strLine.replace('\n', '')

        if strLine.isdigit():
            _EARLIEST_TIMESTAMP_BUS_COULD_TAKE = int(strLine)
        else:
            # Buses
            buses = strLine.split(',')
            # Bus Ids
            strLine = strLine.replace(',x','')
            busIds = strLine.split(',')
            busIds = list(map(int, busIds))
            _NUMBER_BUSES = len(buses)


    for i in range(0, len(buses)):
        if buses[i].isdigit():
            timeStamps[int(buses[i])] = {'offset': i, 'timestamp': 0}
            _ALL_BUS_ID_MULTIPLICATION *= int(buses[i])




readBusData()
print("Earliest timestamp bus could take {0}".format(_EARLIEST_TIMESTAMP_BUS_COULD_TAKE))
print("Number of Buses {0}. Buses {1}".format(_NUMBER_BUSES, buses))
if (len(sys.argv) == 2 and sys.argv[1] == '1') or len(sys.argv) == 1:
    # First Exercise
    print('First Exercise')
    start_time = time.time()
    result = getEarliestIDBusMultiplyTimeWait()
    print("\t - Result: {0}. Time: {1}s".format(result, time.time() - start_time))

if (len(sys.argv) == 2 and sys.argv[1] == '2') or len(sys.argv) == 1:
    # Second Exercise
    print('Second Exercise')
    start_time = time.time()
    result = parallelEarlyTimestampSubsequent()
    print("\t - Result: {0}. Time: {1}s".format(result, time.time() - start_time))
