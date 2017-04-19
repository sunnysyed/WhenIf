#Algorithm can be implemented very simply.
#Just sort classes based on priority.
#Priority will be 1-8 calculated based on how often a class is offered within 2 years.
#Priority is already given to classes here, but can be easily calculated during data creation.


# - - - - - CLASSES - - - - - #

class Degree:
    def __init__(self, code, name, concentrations):
        self.code = code
        self.name = name
        self.concentrations = concentrations

class Concentration:
    def __init__(self, name, link, classes):
        self.name = name
        self.link = link
        self.classes = classes

class Class:
    def __init__(self, code, name, intro, prereqs, sections, priority):
        self.code = code
        self.name = name
        self.intro = intro
        self.prereqs = prereqs
        self.sections = sections
        self.priority = priority

class Section:
    def __init__(self, code, quarter, online, days, time):
        self.code = code
        self.quarter = quarter
        self.online = online
        self.days = days
        self.time = time

# - - - - - TEST DATA - - - - - #

CS = Degree(300, 'Computer Science', [])

CSC = Concentration('', '/academics/Pages/Current/Requirements-MS-in-Computer-Science.aspx', [])
CS.concentrations.append(CSC)

CSC400 = Class(400, 'Discrete Structures for Computer Science', True, [], [], 1)
CSC400.sections.append(Section(901, 'Spring', False, ['Th'], [1745, 2100]))
CSC400.sections.append(Section(910, 'Spring', True, [], []))
CSC.classes.append(CSC400)

CSC401 = Class(401, 'Introduction to Programming', True, [], [], 1)
CSC401.sections.append(Section(901, 'Spring', False, ['Tu'], [1745, 2100]))
CSC401.sections.append(Section(910, 'Spring', True, [], []))
CSC401.sections.append(Section(902, 'Spring', False, ['Th'], [1745, 2100]))
CSC401.sections.append(Section(911, 'Spring', True, [], []))
CSC.classes.append(CSC401)

CSC402 = Class(402, 'Data Structures I', True, [], [], 1)
CSC402.sections.append(Section(901, 'Spring', False, ['Tu'], [1745, 2100]))
CSC402.sections.append(Section(910, 'Spring', True, [], []))
CSC.classes.append(CSC402)

CSC403 = Class(403, 'Data Structures II', True, [], [], 1)
CSC403.sections.append(Section(901, 'Spring', False, ['Tu'], [1745, 2100]))
CSC403.sections.append(Section(910, 'Spring', True, [], []))
CSC403.sections.append(Section(902, 'Spring', False, ['W'], [1745, 2100]))
CSC403.sections.append(Section(912, 'Spring', True, [], []))
CSC.classes.append(CSC403)

CSC406 = Class(406, 'Systems I', True, [], [], 1)
CSC406.sections.append(Section(901, 'Spring', False, ['M'], [1745, 2100]))
CSC406.sections.append(Section(910, 'Spring', True, [], []))
CSC.classes.append(CSC406)

CSC407 = Class(407, 'Systems II', True, [], [], 1)
CSC407.sections.append(Section(901, 'Spring', False, ['M'], [1745, 2100]))
CSC407.sections.append(Section(902, 'Spring', False, ['Th'], [1745, 2100]))
CSC407.sections.append(Section(911, 'Spring', True, [], []))
CSC.classes.append(CSC407)

# - - - - - ALGORITHM - - - - - #
taken = []

CSC.classes.sort(key=lambda c: c.priority)

print(CS.name)
for co in CS.concentrations:
    print(co.name)
    for cl in co.classes:
        print(cl.name)
        for s in cl.sections:
            print(s.code)
