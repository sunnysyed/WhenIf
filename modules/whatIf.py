# - - - - - IMPORTS - - - - - #

##from seed import concentrationDict
##from seed import classDict
from collections import OrderedDict

# - - - - - FUNCTIONS - - - - - #

def whatIf(degree, concentration, start, classAmount, taken):
    seasons = ['Fall', 'Winter', 'Spring', 'Summer']
    classOrder = OrderedDict()
    for z in concentrationDict[concentration].classes:
        classOrder[z] = classDict[z]
    classOrder = OrderedDict(sorted(classOrder.iteritems(), key=lambda c: c[1].priority))

    final = []
    season = 0
    electiveCount = concentrationDict[concentration].electiveCount
    MECCount = 0
    
    if (degree == 'Computer Science') or concentration == "Standard Concentration":
        MEC = []

    elif concentration == "Business Analysis/Systems Analysis Concentration":
        MEC = ['ECT 424', 'ECT 480', 'HCI 440', 'IS 431', 'IS 440', 'IS 455', 'IS 540', 'IS 556', 'IS 565', 'IS 578']

    elif concentration == "Business Intelligence Concentration":
        MEC = ['CSC 424', 'CSC 495', 'CSC 575', 'ECT 584', 'GEO 441', 'HCI 512', 'IPD 451', 'IS 452', 'IS 536', 'IS 550']

    elif concentration == "Database Administration Concentration":
        MEC = ['CNS 440', 'IPD 451', 'IS 452', 'IS 505', 'IS 536', 'IS 550']

    elif concentration == "IT Enterprise Management Concentration":
        MEC = ['CNS 440', 'ECT 556', 'IS 440', 'IS 483', 'IS 500', 'MGT 500', 'IS 505', 'IS 506', 'IS 535', 'IS 536', 'IS 540', 'IS 550', 'IS 560', 'IS 565', 'IS 579', 'IS 580']

    fastest(classOrder, seasons, classAmount, taken, season, MEC, final, electiveCount, MECCount)
                      
##    print("DEGREE: " + degree)
##    print("CONCENTRATION: " + concentration)
##    for cl in final:
##        print(cl)

    return final

def fastest(classOrder, seasons, classAmount, taken, season, MEC, final, electiveCount, MECCount):
    while len(classOrder) > 0:
        for cl in classOrder:
            isMEC = (classOrder[cl].code in MEC)
            MECDone = isMEC and (MECCount >= 3)
            if MECDone:
                del classOrder[cl]
            elif (classOrder[cl].priority == 0) or ((seasons[(season/classAmount)%4] in classOrder[cl].terms) and check_pres(classOrder[cl], taken)):
               final.append(classOrder[cl].name)
               taken.append(classOrder[cl].code)
               del classOrder[cl]
               season+=1
               if isMEC:
                   MECCount+=1
        if len(classOrder) > 0:
            if electiveCount > 0:
                final.append('Elective')
                electiveCount-=1
                season+=1
            else:
                for item in classOrder:
##                    print classOrder[cl].name
##                    #print classOrder[cl].prereqs
##                    print classOrder[cl].terms
##                    print classOrder[cl].priority
##                    print seasons[(season/classAmount)%4]
                    final.append('Empty')
                    season+=1
    while electiveCount > 0:
        final.append('Elective')
        electiveCount-=1
        season+=1
    return final

def check_pres(cl, taken):
    choice = False
    if cl.prereqs == None:
        return True
    for x in cl.prereqs:
        if isinstance(x, list):
            for y in x:
                if y in taken:
                    choice = True
            if not choice:
                return False
        elif x not in taken:
            return False
    return True
                                                        
# - - - - - RUN PROGRAM - - - - - #

##whatIf('Computer Science', "Computer Science", 'Fall', 4, [])
##whatIf("Information Systems", "Business Analysis/Systems Analysis Concentration", 'Fall', 4)
##whatIf("Information Systems", "Business Intelligence Concentration", 'Fall', 4, [])
##whatIf("Information Systems", "Database Administration Concentration", 'Fall', 4, [])
##whatIf("Information Systems", "IT Enterprise Management Concentration", 'Fall', 4, [])
##whatIf("Information Systems", "Standard Concentration", 'Fall', 4, [])
