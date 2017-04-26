# - - - - - IMPORTS - - - - - #

import random
import string
import re
import urllib2
from bs4 import BeautifulSoup
import time
import urllib
import json

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
    def __init__(self, code, name, isIntro, prereqs, terms, inClassOnly, onlineOnly, priority):
        self.code = code
        self.name = name
        self.isIntro = isIntro
        self.prereqs = prereqs
        self.terms = terms
        self.inClassOnly = inClassOnly
        self.onlineOnly = onlineOnly
        self.priority = priority

# - - - - - DATA LINKS - - - - - #

base = "http://www.cdm.depaul.edu"

classLinks = {}

classDict = {}

classLinks['IS'] = "http://odata.cdm.depaul.edu/Cdm.svc/Courses?$orderby=CatalogNbr&$filter=EffStatus%20eq%20%27A%27%20and%20SubjectId%20eq%27IS%27&$format=json"

classLinks['CSC'] = "http://odata.cdm.depaul.edu/Cdm.svc/Courses?$orderby=CatalogNbr&$filter=EffStatus%20eq%20%27A%27%20and%20SubjectId%20eq%27CSC%27&$format=json"

classLinks['ECT'] = "http://odata.cdm.depaul.edu/Cdm.svc/Courses?$orderby=CatalogNbr&$filter=EffStatus%20eq%20%27A%27%20and%20SubjectId%20eq%27ECT%27&$format=json"

classLinks['CNS'] = "http://odata.cdm.depaul.edu/Cdm.svc/Courses?$orderby=CatalogNbr&$filter=EffStatus%20eq%20%27A%27%20and%20SubjectId%20eq%27CNS%27&$format=json"

classLinks['HCI'] = "http://odata.cdm.depaul.edu/Cdm.svc/Courses?$orderby=CatalogNbr&$filter=EffStatus%20eq%20%27A%27%20and%20SubjectId%20eq%27HCI%27&$format=json"

classLinks['SE'] = "http://odata.cdm.depaul.edu/Cdm.svc/Courses?$orderby=CatalogNbr&$filter=EffStatus%20eq%20%27A%27%20and%20SubjectId%20eq%27SE%27&$format=json"

classLinks['GEO'] = "http://odata.cdm.depaul.edu/Cdm.svc/Courses?$orderby=CatalogNbr&$filter=EffStatus%20eq%20%27A%27%20and%20SubjectId%20eq%27GEO%27&$format=json"

classLinks['IPD'] = "http://odata.cdm.depaul.edu/Cdm.svc/Courses?$orderby=CatalogNbr&$filter=EffStatus%20eq%20%27A%27%20and%20SubjectId%20eq%27IPD%27&$format=json"

classLinks['MGT'] = "http://odata.cdm.depaul.edu/Cdm.svc/Courses?$orderby=CatalogNbr&$filter=EffStatus%20eq%20%27A%27%20and%20SubjectId%20eq%27MGT%27&$format=json"

for key in classLinks:
    classDict[key] = []

# - - - - - FUNCTIONS - - - - - #

def get_Degrees():
    degrees = []

    #IS
    url = base + "/academics/Pages/MSInInformationSystems.aspx"
    soup = get_soup_from_url(url)
    ISConcentrations = []
    for li in soup.findAll("ul", { "class" : "sub-nav" })[0].findAll('li'):
        concentration = Concentration(li.a.text, li.a['href'], [])
        ISConcentrations.append(concentration)
    degrees.append(Degree(soup.findAll("span", { "class" : "breadcrumbCurrent" })[0].text, ISConcentrations))
    
    #CSC
    url = base + "/academics/Pages/MSInComputerScience.aspx"
    soup = get_soup_from_url(url)
    CSCConcentrations = []
    CSCConcentrations.append(Concentration("MS in Computer Science", "/academics/Pages/Current/Requirements-MS-in-Computer-Science.aspx", []))
    degrees.append(Degree(soup.findAll("span", {"class": "breadcrumbCurrent"})[0].text, CSCConcentrations))

    return degrees

def get_prereqs(DescrLong):
    #"PREREQUISITE(S)" are structured in varying formats in data, so currently only returns string.
    #Will need to make a more in-depth parser to solve this.
    if DescrLong is None:
        return []
    if "PREREQUISITE(S)" in DescrLong:
        return DescrLong.split("PREREQUISITE(S)")[1]

def get_terms():
    #Will parse "TypicallyOffered" data.
    return

def get_priority():
    #get_terms must be finished first.
    return

def get_Classes(links):
    for x in links:
        response = urllib.urlopen(links[x])
        data = json.loads(response.read())
        for y in data['d']['results']:
            classDict[x].append(Class(y['CatalogNbr'], y["CourseTitleLong"], False, get_prereqs(y["DescrLong"]), y["TypicallyOffered"], y["IsInClassOnly"], y["IsOnlineOnly"], 0))

def get_soup_from_url(url):
    opener = urllib2.build_opener()
    url_opener = opener.open(url)
    page = url_opener.read()
    soup = BeautifulSoup(page, "html.parser")
    return soup

# - - - - - RUN PROGRAM - - - - - #
 
degrees = get_Degrees()

get_Classes(classLinks)

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

##for x in degrees:
##    print x.name
##    for y in x.concentrations:
##        print y.name
