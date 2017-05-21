# - - - - - IMPORTS - - - - - #
<<<<<<< HEAD:modules/whenIf.py

from seed import getSeedData
=======
>>>>>>> refs/remotes/origin/dev:modules/whatIf.py
from collections import OrderedDict

# - - - - - FUNCTIONS - - - - - #

<<<<<<< HEAD:modules/whenIf.py
def whenIf(degree, concentration, start, classAmount, taken, seedData, takenIntros):
=======
def whatIf(degree, concentration, start, classAmount, taken, seedData):
>>>>>>> refs/remotes/origin/dev:modules/whatIf.py
    concentrationDict = seedData['concentrations']
    classDict = seedData['classes']
    seasons = ['Fall', 'Winter', 'Spring', 'Summer']
    classOrder = OrderedDict()
    for z in concentrationDict[concentration].classes:
        classOrder[z] = classDict[z]
    classOrder = OrderedDict(sorted(classOrder.iteritems(), key=lambda c: c[1].priority))

    final = []
    season = 0
    electiveCount = concentrationDict[concentration].electiveCount
    MECCount = 0
    MEC = []
    
    if (degree == 'Computer Science') or concentration == "Standard Concentration":
        MEC = []
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

<<<<<<< HEAD:modules/whenIf.py
    fastest(classOrder, seasons, classAmount, taken, season, MEC, final, electiveCount, MECCount, takenIntros, requiredIntros)
=======
    fastest(classOrder, seasons, classAmount, taken, season, MEC, final, electiveCount, MECCount)
>>>>>>> refs/remotes/origin/dev:modules/whatIf.py

    return final

def fastest(classOrder, seasons, classAmount, taken, season, MEC, final, electiveCount, MECCount, takenIntros, requiredIntros):
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
            elif (seasons[(season/classAmount)%4] in classOrder[cl].terms) and check_pres(classOrder[cl], taken, waivedIntros):
                if (classOrder[cl].priority == 0) and (takenIntros):
                    del classOrder[cl]
                else:
                    final.append(classOrder[cl].name)
                    takenTemp.append(classOrder[cl].code)
                    del classOrder[cl]
                    season+=1
                    if isMEC:
                        MECCount+=1
        for x in takenTemp:
            taken.append(x)
        if len(classOrder) > 0:
            if electiveCount > 0:
                final.append('Elective')
                electiveCount-=1
                season+=1
            else:
                for item in classOrder:
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
