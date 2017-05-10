# - - - - - IMPORTS - - - - - #

import random
import string
import re
import urllib2
from bs4 import BeautifulSoup
import time
import urllib
import json
from collections import OrderedDict

# - - - - - CLASSES - - - - - #

class Degree:
    def __init__(self, name, concentrations):
        self.name = name
        self.concentrations = concentrations

class Concentration:
    def __init__(self, name, link, classes):
        self.name = name
        self.link = link
        self.classes = classes

class Class:
    def __init__(self, code, name, isIntro, prereqs, terms, inClassOnly, onlineOnly, priority, OR):
        self.code = code
        self.name = name
        self.isIntro = isIntro
        self.prereqs = prereqs
        self.terms = terms
        self.inClassOnly = inClassOnly
        self.onlineOnly = onlineOnly
        self.priority = priority
        self.OR = OR

# - - - - - DATA LINKS - - - - - #

base = "http://www.cdm.depaul.edu"

classLinks = {}

concentrationDict = OrderedDict()

classDict = OrderedDict()

classLinks['IS'] = "http://odata.cdm.depaul.edu/Cdm.svc/Courses?$orderby=CatalogNbr&$filter=EffStatus%20eq%20%27A%27%20and%20SubjectId%20eq%27IS%27&$expression=json"

classLinks['CSC'] = "http://odata.cdm.depaul.edu/Cdm.svc/Courses?$orderby=CatalogNbr&$filter=EffStatus%20eq%20%27A%27%20and%20SubjectId%20eq%27CSC%27&$expression=json"

classLinks['ECT'] = "http://odata.cdm.depaul.edu/Cdm.svc/Courses?$orderby=CatalogNbr&$filter=EffStatus%20eq%20%27A%27%20and%20SubjectId%20eq%27ECT%27&$expression=json"

classLinks['CNS'] = "http://odata.cdm.depaul.edu/Cdm.svc/Courses?$orderby=CatalogNbr&$filter=EffStatus%20eq%20%27A%27%20and%20SubjectId%20eq%27CNS%27&$expression=json"

classLinks['HCI'] = "http://odata.cdm.depaul.edu/Cdm.svc/Courses?$orderby=CatalogNbr&$filter=EffStatus%20eq%20%27A%27%20and%20SubjectId%20eq%27HCI%27&$expression=json"

classLinks['SE'] = "http://odata.cdm.depaul.edu/Cdm.svc/Courses?$orderby=CatalogNbr&$filter=EffStatus%20eq%20%27A%27%20and%20SubjectId%20eq%27SE%27&$expression=json"

classLinks['GEO'] = "http://odata.cdm.depaul.edu/Cdm.svc/Courses?$orderby=CatalogNbr&$filter=EffStatus%20eq%20%27A%27%20and%20SubjectId%20eq%27GEO%27&$expression=json"

classLinks['IPD'] = "http://odata.cdm.depaul.edu/Cdm.svc/Courses?$orderby=CatalogNbr&$filter=EffStatus%20eq%20%27A%27%20and%20SubjectId%20eq%27IPD%27&$expression=json"

classLinks['MGT'] = "http://odata.cdm.depaul.edu/Cdm.svc/Courses?$orderby=CatalogNbr&$filter=EffStatus%20eq%20%27A%27%20and%20SubjectId%20eq%27MGT%27&$expression=json"

classLinks['IT'] = "http://odata.cdm.depaul.edu/Cdm.svc/Courses?$orderby=CatalogNbr&$filter=EffStatus%20eq%20%27A%27%20and%20SubjectId%20eq%27IT%27&$expression=json"

# - - - - - FUNCTIONS - - - - - #

def get_Degrees():
    degrees = []

    #IS
    url = base + "/academics/Pages/MSInInformationSystems.aspx"
    soup = get_soup_from_url(url)
    ISConcentrations = []
    for li in soup.findAll("ul", { "class" : "sub-nav" })[0].findAll('li'):
        concentration = Concentration(li.a.text, li.a['href'], [])
        concentrationDict[li.a.text] = concentration
        ISConcentrations.append(li.a.text)
    degrees.append(Degree(soup.findAll("span", { "class" : "breadcrumbCurrent" })[0].text, ISConcentrations))
    
    #CSC
    url = base + "/academics/Pages/MSInComputerScience.aspx"
    soup = get_soup_from_url(url)
    CSCConcentration = Concentration("MS in Computer Science", "/academics/Pages/Current/Requirements-MS-in-Computer-Science.aspx", [])
    concentrationDict["MS in Computer Science"] = CSCConcentration
    degrees.append(Degree(soup.findAll("span", {"class": "breadcrumbCurrent"})[0].text, ["MS in Computer Science"]))

    return degrees

def get_priority():
    #get_terms must be finished first.
    return

def get_prereqs(DescrLong):
    #"PREREQUISITE(S)" are structured in varying expressions in data, so currently only returns string.
    #Will need to make a more in-depth parser to solve this.
    prereqs = []
    if DescrLong is None:
        return prereqs
    if "PREREQUISITE(S)" in DescrLong:
        x = DescrLong.split("PREREQUISITE(S)")[1]
        try:
            x = x.split(": ")[1].lstrip()
        except:
            pass
        #'Class AND (Class or ... or Class)'
        pattern = re.compile('[A-Z]+ [0-9]{3} (AND)|(and) \([[A-Z]+ [0-9]{3} (or)?]+\)')
        expression = pattern.match(x)
        if expression:
            text = expression.group().split()
            print text
            prereqs.append(text[0] + ' ' + text[1])
            count = 3
            while count < len(text):
                prereqs.append(text[count] + ' ' + text[count+1])
                count+=3
            return prereqs
        #'Class AND Class'
        pattern = re.compile('[A-Z]+ [0-9]{3} (AND)|(and) [A-Z]+ [0-9]{3}')
        expression = pattern.match(x)
        if expression:
            text = expression.group().split()
            print text
            prereqs.append(text[0] + ' ' + text[1])
            prereqs.append(text[3] + ' ' + text[4])
            return prereqs
        #'Class'
        pattern = re.compile('[A-Z]+ [0-9]{3}')
        expression = pattern.match(x)
        if expression:
            prereqs.append(expression.group())
        return prereqs

def get_terms(TypicallyOffered):
    #Will parse "TypicallyOffered" data.
    #print(TypicallyOffered)
    return

def get_Classes(links):
    for x in links:
        response = urllib.urlopen(links[x])
        data = json.loads(response.read())
        for y in data['d']['results']:
            classDict[x + ' ' + y['CatalogNbr']] = Class(y['CatalogNbr'], y["CourseTitleLong"], False, get_prereqs(y["DescrLong"]), get_terms(y["TypicallyOffered"]), y["IsInClassOnly"], y["IsOnlineOnly"], 0, None)

def put_classes():
    for x in degrees:
        for y in x.concentrations:
            url = base + concentrationDict[y].link
            soup = get_soup_from_url(url)
            count = 0
            total = len(soup.findAll("table", { "class" : "courseList" }))
            if x == degrees[1]:
                total = 2
            while count < total:
                for tr in soup.findAll("table", { "class" : "courseList" })[count].findAll('tbody'):
                    for z in tr:
                        for a in z:
                            for b in a:
                                if b.find('OR') == -1:    
                                    try:
                                        b = b.rstrip()
                                    except:
                                        pass
                                    if b in classDict:
                                        concentrationDict[y].classes.append(b)
                                else:
                                    for c in b:
                                        if c in classDict:
                                            position = len(concentrationDict[y].classes)
                                            previous = concentrationDict[y].classes[position-1]
                                            concentrationDict[y].classes.append(c)
                                            classDict[c].OR = previous
                                            classDict[previous].OR = c
                count+=1

def get_soup_from_url(url):
    opener = urllib2.build_opener()
    url_opener = opener.open(url)
    page = url_opener.read()
    soup = BeautifulSoup(page, "html.parser")
    return soup

# - - - - - RUN PROGRAM - - - - - #
 
degrees = get_Degrees()

get_Classes(classLinks)

put_classes()

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

#print classLinks
#print classDict

for x in degrees:
    print x.name
    for y in x.concentrations:
        print concentrationDict[y].name
        for z in concentrationDict[y].classes:
            #print classDict[z].name
            print classDict[z].prereqs
