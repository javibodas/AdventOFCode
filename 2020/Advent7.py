import sys
_NUM_POLICIES = 0
luggagesPolicies = []
luggagesWithoutPolicy = []
luggagesWithShinyGold = []
shinyGoldLuggage = {}
_SHINY_GOLD_BAG = 'shiny gold'


def getFathersLuggages(childsBag):

    global luggagesPolicies
    global luggagesWithShinyGold
    listFathers = []

    for childBag in childsBag:
        for luggage in luggagesPolicies:
            if childBag in luggage['childsBag'].keys() and luggage['fatherBag'] not in luggagesWithShinyGold and luggage['fatherBag'] not in listFathers:
                listFathers.append(luggage['fatherBag'])

    if len(listFathers) > 0:
        luggagesWithShinyGold = luggagesWithShinyGold + listFathers
        return childsBag + getFathersLuggages(listFathers)
    else:
        return childsBag

def getLuggageByNameFather(fatherBagName):
    global luggagesPolicies
    global luggagesWithoutPolicy

    tmpListFilter = filter(lambda luggage: luggage['fatherBag'] == fatherBagName, luggagesPolicies)
    if(len(tmpListFilter) == 0):
        tmpListFilter = filter(lambda luggage: luggage['fatherBag'] == fatherBagName, luggagesWithoutPolicy)

    return tmpListFilter[0]

def getNumberLuggages(fatherLuggage):

    if 'childsBag' not in fatherLuggage.keys():
        return 0

    counter = 0

    for childLuggage in fatherLuggage['childsBag'].keys():
        counter = counter + int(fatherLuggage['childsBag'][childLuggage]) + int(fatherLuggage['childsBag'][childLuggage]) * getNumberLuggages(getLuggageByNameFather(childLuggage)) 
    
    return counter



def readFileLuggage():
    global luggagesPolicies
    global luggagesWithoutPolicy
    global shinyGoldLuggage
    global _NUM_POLICIES

    f = open("Advent7.txt", "r")

    for strLine in f:

        # Remove break lines
        if '\r' in strLine:
            strLine = strLine.replace('\r', '')
        if '\n' in strLine:
           strLine = strLine.replace('\n', '')

        # Line treatment and obtain father bags and contains bags
        strLine = strLine.lower()
        bagContainsList = strLine.split(' contain ')
        bagFather = bagContainsList[0]
        bagChilds = bagContainsList[1]

        # Father bag
        bagFather = bagFather.replace(' bags', '')
        
        if('no other bags' in bagChilds):
            luggagesWithoutPolicy.insert(_NUM_POLICIES,{'fatherBag': bagFather})
            continue
        else:
            luggagesPolicies.insert(_NUM_POLICIES,{'fatherBag': bagFather})

        # Childs bags
        bagChilds = bagChilds.replace('.', '')
        bagChilds = bagChilds.split(', ')

        for cBag in bagChilds:
            if 'bags' in cBag:
                childBag = cBag.replace(' bags', '')
            elif 'bag' in cBag:
                childBag = cBag.replace(' bag', '')

            childBagElements = childBag.split(' ')
            numberBag = childBagElements[0]
            bag = childBagElements[1] + ' ' + childBagElements[2]

            if 'childsBag' not in luggagesPolicies[_NUM_POLICIES].keys():
                luggagesPolicies[_NUM_POLICIES]['childsBag'] = {}
                luggagesPolicies[_NUM_POLICIES]['childsBag'][bag] = numberBag
            elif childBag not in luggagesPolicies[_NUM_POLICIES]['childsBag'].keys():
                luggagesPolicies[_NUM_POLICIES]['childsBag'][bag] = numberBag
            elif childBag in luggagesPolicies[_NUM_POLICIES]['childsBag'].keys():
                luggagesPolicies[_NUM_POLICIES]['childsBag'][bag] = numberBag + luggagesPolicies[_NUM_POLICIES]['childsBag'][bag]

            if bag == _SHINY_GOLD_BAG:
                luggagesWithShinyGold.append(luggagesPolicies[_NUM_POLICIES]['fatherBag'])

        #Exercise 2. Create dictionarie of 'shiny gold' bag
        if bagFather == _SHINY_GOLD_BAG:
            shinyGoldLuggage = luggagesPolicies[_NUM_POLICIES]
        
        _NUM_POLICIES = _NUM_POLICIES + 1

readFileLuggage()
print("Number of policies: {0}".format(_NUM_POLICIES))
if (len(sys.argv) == 2 and sys.argv[1] == '1') or len(sys.argv) == 1:
    # First Exercise
    print('First Exercise')
    print("\t Result: {0}".format(len(getFathersLuggages(luggagesWithShinyGold))))
if (len(sys.argv) == 2 and sys.argv[1] == '2') or len(sys.argv) == 1:
    # Second Exercise
    print('Second Exercise')
    print("\t Result: {0}".format(getNumberLuggages(shinyGoldLuggage)))
