#Current replacement for scraper.

#Some member variables ended up not getting used at all in the alogrithm,
#so I will clean things up in the future.

# - - - - - IMPORTS - - - - - #

from collections import OrderedDict

# - - - - - CLASSES - - - - - #

class Degree:
    def __init__(self, name, concentrations):
        self.name = name
        self.concentrations = concentrations

class Concentration:
    def __init__(self, name, link, classes, electiveCount):
        self.name = name
        self.link = link #NOT NECESSARY
        self.classes = classes
        self.electiveCount = electiveCount

class Class:
    def __init__(self, code, name, isIntro, prereqs, terms, inClassOnly, onlineOnly, priority, OR):
        self.code = code
        self.name = name
        self.isIntro = isIntro #NOT NECESSARY
        self.prereqs = prereqs
        self.terms = terms
        self.inClassOnly = inClassOnly
        self.onlineOnly = onlineOnly #NOT NECESSARY
        self.priority = priority
        self.OR = OR #NOT NECESSARY

# - - - - - DATA STORAGE - - - - - #

#Link to data source: http://www.cdm.depaul.edu/academics/Pages/MSInInformationSystems.aspx

degrees = []

concentrationDict = OrderedDict()

classDict = OrderedDict()

# - - - - - DATA - - - - - #

#Degrees
degrees.append(Degree("Information Systems", []))
degrees.append(Degree("Computer Science", []))

#Concentrations
concentrationDict["Business Analysis/Systems Analysis Concentration"] = Concentration("Business Analysis/Systems Analysis Concentration", "http://www.cdm.depaul.edu/academics/Pages/Current/Requirements-MS-IS-Business-Systems-Analysis.aspx", [], 1)
concentrationDict["Business Intelligence Concentration"] = Concentration("Business Intelligence Concentration", "http://www.cdm.depaul.edu/academics/Pages/Current/Requirements-MS-IS-Business-Intelligence.aspx", [], 1)
concentrationDict["Database Administration Concentration"] = Concentration("Database Administration Concentration", "http://www.cdm.depaul.edu/academics/Pages/Current/Requirements-MS-IS-Database-Administration.aspx", [],1)
concentrationDict["IT Enterprise Management Concentration"] = Concentration("IT Enterprise Management Concentration", "http://www.cdm.depaul.edu/academics/Pages/Current/Requirements-MS-IS-IT-Enterprise-Management.aspx", [], 1)
concentrationDict["Standard Concentration"] = Concentration("Standard Concentration", "http://www.cdm.depaul.edu/academics/Pages/Current/Requirements-MS-IS-Standard.aspx", [], 8)

for x in concentrationDict:
    degrees[0].concentrations.append(x)

concentrationDict["Computer Science"] = Concentration("Computer Science", "http://www.cdm.depaul.edu/academics/Pages/Current/Requirements-MS-in-Computer-Science.aspx", [], 8)

degrees[1].concentrations.append(concentrationDict["Computer Science"].name)

#Classes

classDict['IS 421'] = Class('IS 421', 'Systems Analysis', False, None, ['Fall', 'Summer', 'Spring', 'Winter'], False, False, 4, None)
classDict['CSC 451'] = Class('CSC 451', 'Database Design', False, None, ['Fall', 'Summer', 'Spring', 'Winter'], False, False, 4, None)
classDict['IS 422'] = Class('IS 422', 'System Design, Implementation, and Maintenance', False, ['IS 421', 'CSC 451'], ['Fall', 'Spring', 'Winter'], False, False, 3, None)
classDict['IS 430'] = Class('IS 430', 'Fundamentals of IT Project Management', False, None, ['Fall', 'Spring', 'Winter', 'Summer'], False, False, 4, None)
classDict['CNS 440'] = Class('CNS 440', 'Information Security Management', False, None, ['Fall', 'Spring', 'Winter'], False, False, 3, None)
classDict['IS 435'] = Class('IS 435', 'Organizational Modeling', False, [['IS 421', 'SE 430']], ['Fall', 'Spring'], False, False, 2, None)
classDict['IS 485'] = Class('IS 485', 'Requirements Elicitation, Analysis, and Specification', False, [['IS 422', 'IS 430', 'PM 430']], ['Winter'], False, False, 1, None)
classDict['IS 535'] = Class('IS 535', 'Information Technology Investment Financial Analysis', False, [['SE 477', 'IS 565', 'ACCT 500', 'IS 430', 'PM 430', 'ECT 455']], ['Winter', 'Fall', 'Spring'], False, False, 3, None)
classDict['IS 560'] = Class('IS 560', 'Enterprise Systems', False, None, ['Fall', 'Spring'], False, False, 2, None)
classDict['ECT 424'] = Class('ECT 424', 'Enterprise Infrastructure', False, None, ['Fall', 'Spring', 'Summer', 'Winter'], False, False, 4, None)
classDict['ECT 480'] = Class('ECT 480', 'Intranets and Portals', False, ['ECT 424'], ['Spring'], False, False, 1, None)
classDict['HCI 440'] = Class('HCI 440', 'Introduction to User-Centered Design', False, None, ['Spring', 'Fall', 'Summer', 'Winter'], False, False, 4, None)
classDict['IS 431'] = Class('IS 431', 'Digital Product Management', False, None, ['Fall', 'Winter'], False, False, 2, None)
classDict['IS 440'] = Class('IS 440', 'Collaborative Technologies for Leading Projects', False, None, ['Fall', 'Winter', 'Spring', 'Summer'], False, False, 4, None)
classDict['IS 455'] = Class('IS 455', 'Electronic Business', False, None, ['Fall', 'Spring'], False, False, 2, None)
classDict['IS 540'] = Class('IS 540', 'Global Information Technology', False, None, ['Winter'], False, False, 1, None)
classDict['IS 556'] = Class('IS 556', 'Enterprise Project Management', False, [['IS 430', 'PM 430']], ['Winter', 'Fall', 'Spring'], False, False, 3, None)
classDict['IS 578'] = Class('IS 578', 'Information Technology Consulting', False, None, ['Spring'], False, False, 1, None)
classDict['IS 577'] = Class('IS 577', 'Information Systems Policies and Strategies', False, None, ['Summer', 'Winter'], False, False, 2, None)

classDict['IT 411'] = Class('IT 411', 'Scripting for Interactive Systems', True, None, ['Fall', 'Winter', 'Spring'], False, False, 0, 'CSC 401')
classDict['CSC 401'] = Class('CSC 401', 'Introduction to Programming', True, None, ['Fall', 'Winter', 'Spring', 'Summer'], False, False, 0, 'IT 411')
classDict['IT 403'] = Class('IT 403', 'Statistics and Data Analysis', True, None, ['Fall', 'Winter', 'Spring', 'Summer'], False, False, 0, None)
classDict['IS 574'] = Class('IS 574', 'Business Intelligence', False, ['CSC 451'], ['Fall', 'Winter', 'Spring'], False, False, 3, None)
classDict['CSC 423'] = Class('CSC 423', 'Data Analysis and Regression', False, ['IT 403'], ['Fall', 'Winter', 'Spring', 'Summer'], False, False, 4, None)
classDict['IS 467'] = Class('IS 467', 'Fundamentals of Data Science', False, [['IT 403', 'CSC 423']], ['Fall', 'Winter', 'Spring'], False, False, 3, None)
classDict['IS 549'] = Class('IS 549', 'Data Warehousing', False, [['CSC 451', 'CSC 453', 'CSC 455']], ['Fall', 'Winter'], False, False, 2, None)
classDict['CSC 424'] = Class('CSC 424', 'Advanced Data Analysis', False, ['CSC 423'], ['Fall', 'Winter', 'Summer', 'Spring'], False, False, 4, None)
classDict['CSC 495'] = Class('CSC 495', 'Social Network Analysis', False, [['CSC 423', 'SOC 412']], ['Fall', 'Spring'], False, False, 2, None)
classDict['CSC 575'] = Class('CSC 575', 'Intelligent Information Retrieval', False, ['CSC 403'], ['Winter'], False, False, 1, None)
classDict['ECT 584'] = Class('ECT 584', 'Web Data Mining', False, ['IT 403', ['CSC 451', 'CSC 453', 'CSC 455']], ['Summer', 'Spring', 'Fall'], False, False, 3, None)
classDict['GEO 441'] = Class('GEO 441', 'Geographic Information Systems (Gis) for Community Development', False, None, ['Summer', 'Spring', 'Fall', 'Winter'], True, False, 4, None)
classDict['HCI 512'] = Class('HCI 512', 'Information Visualization and Infographics', False, ['IT 403', 'HCI 470'], ['Fall', 'Winter'], False, False, 2, None)
classDict['IPD 451'] = Class('IPD 451', 'Big Data and NoSQL Program', False, None, ['Fall', 'Winter', 'Spring'], False, False, 3, None)
classDict['IS 452'] = Class('IS 452', 'Big Data and the Internet of Things (Iot)', False, None, ['Fall', 'Spring'], False, False, 2, None)
classDict['IS 536'] = Class('IS 536', 'Enterprise Cloud Computing', False, None, ['Fall', 'Spring', 'Winter'], False, False, 3, None)
classDict['IS 550'] = Class('IS 550', 'Enterprise Data Management', False, [['CSC 451', 'CSC 453', 'CSC 455']], ['Fall'], False, False, 1, None)

classDict['CSC 454'] = Class('CSC 454', 'Database Administration and Management', False, [['CSC 451', 'CSC 453', 'CSC 455']], ['Fall', 'Summer', 'Winter'], False, True, 3, None)
classDict['CSC 452'] = Class('CSC 452', 'Database Programming', False, [['CSC 453', 'CSC 451', 'CSC 455'], ['CSC 401', 'IT 411']], ['Fall', 'Summer', 'Winter', 'Spring'], False, False, 4, None)
classDict['CSC 554'] = Class('CSC 554', 'Advanced Database Management', False, [['CSC 453', 'CSC 454']], ['Winter', 'Spring'], False, False, 2, None)
classDict['IS 505'] = Class('IS 505', 'Business Continuity/Disaster Recovery Theories and Strategies', False, None, ['Winter', 'Spring', 'Fall', 'Summer'], False, False, 4, None)

classDict['IS 570'] = Class('IS 570', 'Enterprise System Implementation', False, [['IS 430', 'PM 430']], ['Winter', 'Fall', 'Summer'], False, False, 3, None)
classDict['ECT 556'] = Class('ECT 556', 'Enterprise Architecture and Design', False, ['ECT 424', 'SE 430'], ['Spring'], False, False, 1, None)
classDict['IS 483'] = Class('IS 483', 'Information Services and Operations', False, None, ['Winter'], False, False, 1, None)
classDict['IS 500'] = Class('IS 500', 'Information Technology Leadership', False, [['IS 430', 'PM 430', 'SE 477']], ['Spring', 'Fall'], False, False, 2, 'MGT 500')
classDict['MGT 500'] = Class('MGT 500', 'Managing for Effective and Ethical Organizational Behavior', False, None, ['Spring', 'Fall', 'Summer', 'Winter'], False, False, 4, 'IS 500')
classDict['IS 506'] = Class('IS 506', 'Business Continuity/Disaster Recovery Management and Tactics', False, ['IS 505'], ['Summer', 'Winter'], False, False, 2, None)
classDict['IS 565'] = Class('IS 565', 'IT Outsourcing', False, None, ['Spring', 'Winter'], False, False, 2, None)
classDict['IS 579'] = Class('IS 579', 'Virtual Software Teams Management', False, [['PM 430', 'IS 430']], ['Spring'], True, False, 1, None)
classDict['IS 580'] = Class('IS 580', 'Technology Entrepreneurship', False, None, ['Spring', 'Fall'], True, False, 2, None)

classDict['CSC 400'] = Class('CSC 400', 'Discrete Structures for Computer Science', True, None, ['Spring', 'Fall', 'Summer', 'Winter'], False, False, 0, None)
classDict['CSC 402'] = Class('CSC 402', 'Data Structures I', True, ['CSC 401'], ['Spring', 'Fall', 'Summer', 'Winter'], False, False, 0, None)
classDict['CSC 403'] = Class('CSC 403', 'Data Structures II', True, ['CSC 402'], ['Spring', 'Fall', 'Summer', 'Winter'], False, False, 0, None)
classDict['CSC 406'] = Class('CSC 406', 'Systems I', True, ['CSC 401'], ['Spring', 'Fall', 'Summer', 'Winter'], False, False, 0, None)
classDict['CSC 407'] = Class('CSC 407', 'Systems II', True, ['CSC 406', 'CSC 402'], ['Spring', 'Fall', 'Summer', 'Winter'], False, False, 0, None)
classDict['CSC 421'] = Class('CSC 421', 'Applied Algorithms and Structures', False, ['CSC 400', 'CSC 403'], ['Spring', 'Fall', 'Winter'], False, False, 3, None)
classDict['CSC 435'] = Class('CSC 435', 'Distributed Systems I', False, ['CSC 407', 'CSC 403'], ['Spring', 'Fall', 'Winter'], False, False, 3, None)
classDict['CSC 447'] = Class('CSC 447', 'Concepts of Programming Languages', False, ['CSC 406', 'CSC 403'], ['Spring', 'Fall', 'Winter'], False, False, 3, None)
classDict['CSC 453'] = Class('CSC 453', 'Database Technologies', False, ['CSC 403'], ['Spring', 'Fall', 'Winter'], False, False, 3, None)
classDict['SE 450'] = Class('SE 450', 'Object-Oriented Software Development', False, ['CSC 403'], ['Spring', 'Fall', 'Winter', 'Summer'], False, False, 4, None)

concentrationDict["Business Analysis/Systems Analysis Concentration"].classes = ['IS 421', 'CSC 451', 'IS 422', 'IS 430', 'CNS 440', 'IS 435', 'IS 485', 'IS 535', 'IS 560', 'ECT 424', 'ECT 480', 'HCI 440', 'IS 431', 'IS 440', 'IS 455', 'IS 540', 'IS 556', 'IS 565', 'IS 578', 'IS 577']
concentrationDict["Business Intelligence Concentration"].classes = ['CSC 401', 'IT 403', 'IS 421', 'CSC 451', 'IS 422', 'IS 430', 'IS 574', 'CSC 423', 'IS 467', 'IS 549', 'CSC 424', 'CSC 495', 'CSC 575', 'ECT 584', 'GEO 441', 'HCI 512', 'IPD 451', 'IS 452', 'IS 536', 'IS 550', 'IS 577']
concentrationDict["Database Administration Concentration"].classes = ['CSC 401', 'IS 421', 'CSC 451', 'IS 422', 'IS 430', 'IS 549', 'CSC 454', 'CSC 452', 'CSC 554', 'CNS 440', 'IPD 451', 'IS 452', 'IS 505', 'IS 536', 'IS 550', 'IS 577']
concentrationDict["IT Enterprise Management Concentration"].classes = ['IS 421', 'CSC 451', 'IS 422', 'IS 430', 'ECT 424', 'IS 556', 'IS 570', 'IS 535', 'CNS 440', 'ECT 556', 'IS 440', 'IS 483', 'IS 500', 'MGT 500', 'IS 505', 'IS 506', 'IS 535', 'IS 536', 'IS 540', 'IS 550', 'IS 560', 'IS 565', 'IS 579', 'IS 580', 'IS 577']
concentrationDict["Standard Concentration"].classes = ['IS 421', 'CSC 451', 'IS 422', 'IS 430', 'IS 577']
concentrationDict["Computer Science"].classes = ['CSC 400', 'CSC 401', 'CSC 402', 'CSC 403', 'CSC 406', 'CSC 407', 'CSC 421', 'CSC 435', 'CSC 447', 'CSC 453', 'SE 450']

def getSeedData:
    concentrationsAndClasses = {}
    concentrationsAndClasses['concentrations'] = concentrationDict
    concentrationsAndClasses['classes'] = classDict
    return concentrationsAndClasses

# - - - - - DEBUG - - - - - #

##for x in classDict:
##    print x
##    for y in classDict[x]:
##        print y.code
##        print y.name
##        print y.isIntro
##        print y.prereqs
##        print y.terms
##        print y.inClassOnly
##        print y.onlineOnly
##        print y.priority

#print classDict

##for x in degrees:
##    print "DEGREE: " + x.name
##    for y in x.concentrations:
##        print "CONCENTRATION: " + concentrationDict[y].name
##        for z in concentrationDict[y].classes:
##            print "CLASS: " + classDict[z].name
