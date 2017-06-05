# - - - - - IMPORTS - - - - - #

from collections import OrderedDict

# - - - - - FUNCTIONS - - - - - #

def whenIf(degree, concentration, start, classAmount, taken, seedData, takenIntros):
    concentrationDict = seedData['concentrations']
    if concentration == "Standard Concentration":
        if degree == 'Computer Science':
            concentration = 'Computer Science'
    concentrationDict = seedData['concentrations']
    classDict = seedData['classes']
    seasons = ['Fall', 'Winter', 'Spring', 'Summer']
    classOrder = OrderedDict()
    for z in concentrationDict[concentration].classes:
        if classDict[z].code not in taken:
            classOrder[z] = classDict[z]
    classOrder = OrderedDict(sorted(classOrder.iteritems(), key=lambda c: c[1].priority))
    reverseOrder = OrderedDict(reversed(list(classOrder.items())))
    inClassOrder = OrderedDict(classOrder)
    onlineOrder = OrderedDict(classOrder)
    easyOrder = OrderedDict(sorted(classOrder.iteritems(), key=lambda c: c[1].ease))
    
    pathsDict = {}
    takenClasses = list(taken)
    finalShortest = []
    finalLongest = []
    finalInClass = []
    finalOnline = []
    finalEasy = []
    season = 0
    electiveCount = concentrationDict[concentration].electiveCount
    MECCount = 0
    
    if (degree == 'Computer Science') or concentration == "Standard Concentration":
        MEC = []
        if degree == "Information Systems":
            requiredIntros = []
        else:
            requiredIntros = ['CSC 400', 'CSC 401', 'CSC 402', 'CSC 403', 'CSC 406', 'CSC 407']

    elif concentration == "Business Analysis/Systems Analysis Concentration":
        MEC = ['ECT 424', 'ECT 480', 'HCI 440', 'IS 431', 'IS 440', 'IS 455', 'IS 540', 'IS 556', 'IS 565', 'IS 578']
        requiredIntros = []

    elif concentration == "Business Intelligence Concentration":
        MEC = ['CSC 424', 'CSC 495', 'CSC 575', 'ECT 584', 'GEO 441', 'HCI 512', 'IPD 451', 'IS 452', 'IS 536', 'IS 550']
        requiredIntros = ['CSC 401', 'IT 403']

    elif concentration == "Database Administration Concentration":
        MEC = ['CNS 440', 'IPD 451', 'IS 452', 'IS 505', 'IS 536', 'IS 550']
        requiredIntros = ['CSC 401']

    elif concentration == "IT Enterprise Management Concentration":
        MEC = ['CNS 440', 'ECT 556', 'IS 440', 'IS 483', 'IS 500', 'MGT 500', 'IS 505', 'IS 506', 'IS 535', 'IS 536', 'IS 540', 'IS 550', 'IS 560', 'IS 565', 'IS 579', 'IS 580']
        requiredIntros = []
    
    shortest = fastest(classOrder, seasons, classAmount, takenClasses, season, MEC, finalShortest, electiveCount, MECCount, takenIntros, requiredIntros)
    pathsDict['fastest_path'] = shortest
    printClasses(shortest, degree, concentration)
    
    season = 0
    MECCount = 0
    takenClasses = list(taken)
    electiveCount = concentrationDict[concentration].electiveCount
    MECCount = 0

    longestOrder = longest(reverseOrder, seasons, classAmount, takenClasses, season, MEC, finalLongest, electiveCount, MECCount, takenIntros, requiredIntros)
    pathsDict['longest_path'] = longestOrder
    printClasses(longestOrder, degree, concentration)

    season = 0
    MECCount = 0
    takenClasses = list(taken)
    electiveCount = concentrationDict[concentration].electiveCount
    MECCount = 0

    inClassFriendly = inClass(inClassOrder, seasons, classAmount, takenClasses, season, MEC, finalInClass, electiveCount, MECCount, takenIntros, requiredIntros)
    pathsDict['in_class_path'] = inClassFriendly
    printClasses(inClassFriendly, degree, concentration)

    season = 0
    MECCount = 0
    takenClasses = list(taken)
    electiveCount = concentrationDict[concentration].electiveCount
    MECCount = 0

    onlineFriendly = online(onlineOrder, seasons, classAmount, takenClasses, season, MEC, finalOnline, electiveCount, MECCount, takenIntros, requiredIntros)
    pathsDict['online_path'] = onlineFriendly
    printClasses(onlineFriendly, degree, concentration)

    season = 0
    MECCount = 0
    takenClasses = list(taken)
    electiveCount = concentrationDict[concentration].electiveCount
    MECCount = 0

    easiest = fastest(easyOrder, seasons, classAmount, takenClasses, season, MEC, finalEasy, electiveCount, MECCount, takenIntros, requiredIntros)
    pathsDict['easiest_path'] = easiest
    season = 0
    MECCount = 0
    takenClasses = list(taken)
    electiveCount = concentrationDict[concentration].electiveCount
    MECCount = 0
    
    return pathsDict

def fastest(classOrder, seasons, classAmount, takenClasses, season, MEC, final, electiveCount, MECCount, takenIntros, requiredIntros):
    while len(classOrder) > 0:
        takenTemp = []
        waivedIntros = []
        if takenIntros:
            waivedIntros = requiredIntros
        for cl in classOrder:
            isMEC = (classOrder[cl].code in MEC)
            MECDone = isMEC and (MECCount >= 3)
            if MECDone:
                del classOrder[cl]
            elif (seasons[(season/classAmount)%4] in classOrder[cl].terms) and check_pres(classOrder[cl], takenClasses, waivedIntros):
                if (classOrder[cl].priority == 0) and (takenIntros):
                    del classOrder[cl]
                else:
                    final.append(classOrder[cl].__dict__)
                    takenTemp.append(classOrder[cl].code)
                    del classOrder[cl]
                    season+=1
                    if isMEC:
                        MECCount+=1
        for x in takenTemp:
            takenClasses.append(x)
        if len(classOrder) > 0:
            if electiveCount > 0:
                final.append('Elective')
                electiveCount-=1
                season+=1
            else:
                final.append('Empty')
                season+=1
        takenTemp = []
    while electiveCount > 0:
        final.append('Elective')
        electiveCount-=1
        season+=1
    return final

def longest(classOrder, seasons, classAmount, takenClasses, season, MEC, final, electiveCount, MECCount, takenIntros, requiredIntros):
    while len(classOrder) > 0:
        takingClass = False
        takenTemp = []
        waivedIntros = []
        if takenIntros:
            waivedIntros = requiredIntros
        for cl in classOrder:
            isMEC = (classOrder[cl].code in MEC)
            MECDone = isMEC and (MECCount >= 3)
            if MECDone:
                del classOrder[cl]
            elif (seasons[(season/classAmount)%4] in classOrder[cl].terms) and check_pres(classOrder[cl], takenClasses, waivedIntros) and (not takingClass):
                if (classOrder[cl].priority == 0) and (takenIntros):
                    del classOrder[cl]
                else:
                    final.append(classOrder[cl].__dict__)
                    takenTemp.append(classOrder[cl].code)
                    takingClass = True
                    del classOrder[cl]
                    season+=1
                    if isMEC:
                        MECCount+=1
        for x in takenTemp:
            takenClasses.append(x)
        if len(classOrder) > 0:
            if electiveCount > 0:
                final.append('Elective')
                electiveCount-=1
                season+=1
            else:
                final.append('Empty')
                season+=1
        takenTemp = []
    while electiveCount > 0:
        final.append('Elective')
        electiveCount-=1
        season+=1
    return final

def inClass(classOrder, seasons, classAmount, takenClasses, season, MEC, final, electiveCount, MECCount, takenIntros, requiredIntros):
    while len(classOrder) > 0:
        takenTemp = []
        waivedIntros = []
        if takenIntros:
            waivedIntros = requiredIntros
        for cl in classOrder:
            skipOnline = False
            isMEC = (classOrder[cl].code in MEC)
            MECDone = isMEC and (MECCount >= 3)
            if (isMEC and classOrder[cl].onlineOnly):
                skipOnline = True
            if MECDone:
                del classOrder[cl]
            elif (seasons[(season/classAmount)%4] in classOrder[cl].terms) and check_pres(classOrder[cl], takenClasses, waivedIntros) and (not skipOnline):
                if (classOrder[cl].priority == 0) and (takenIntros):
                    del classOrder[cl]
                else:
                    final.append(classOrder[cl].__dict__)
                    takenTemp.append(classOrder[cl].code)
                    del classOrder[cl]
                    season+=1
                    if isMEC:
                        MECCount+=1
        for x in takenTemp:
            takenClasses.append(x)
        if len(classOrder) > 0:
            if electiveCount > 0:
                final.append('Elective')
                electiveCount-=1
                season+=1
            else:
                final.append('Empty')
                season+=1
        takenTemp = []
    while electiveCount > 0:
        final.append('Elective')
        electiveCount-=1
        season+=1
    return final

def online(classOrder, seasons, classAmount, takenClasses, season, MEC, final, electiveCount, MECCount, takenIntros, requiredIntros):
    while len(classOrder) > 0:
        takenTemp = []
        waivedIntros = []
        if takenIntros:
            waivedIntros = requiredIntros
        for cl in classOrder:
            isMEC = (classOrder[cl].code in MEC)
            MECDone = isMEC and (MECCount >= 3)
            if (classOrder[cl].inClassOnly):
                del classOrder[cl]
            elif MECDone:
                del classOrder[cl]
            elif (seasons[(season/classAmount)%4] in classOrder[cl].terms) and check_pres(classOrder[cl], takenClasses, waivedIntros):
                if (classOrder[cl].priority == 0) and (takenIntros):
                    del classOrder[cl]
                else:
                    final.append(classOrder[cl].__dict__)
                    takenTemp.append(classOrder[cl].code)
                    del classOrder[cl]
                    season+=1
                    if isMEC:
                        MECCount+=1
        for x in takenTemp:
            takenClasses.append(x)
        if len(classOrder) > 0:
            if electiveCount > 0:
                final.append('Elective')
                electiveCount-=1
                season+=1
            else:
                final.append('Empty')
                season+=1
        takenTemp = []
    while electiveCount > 0:
        final.append('Elective')
        electiveCount-=1
        season+=1
    return final

def check_pres(cl, taken, waivedIntros):
    choice = False
    if cl.prereqs == None:
        return True
    for x in cl.prereqs:
        if isinstance(x, list):
            for y in x:
                if (y in taken) or (y in waivedIntros):
                    choice = True
            if not choice:
                return False
        elif (x not in taken) and (x not in waivedIntros):
            return False
    return True

def printClasses(classes, degree, concentration):
    print("DEGREE: " + degree)
    print("CONCENTRATION: " + concentration)
    for cl in classes:
        print(cl)
