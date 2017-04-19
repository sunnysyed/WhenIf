#Some experimentation I had done with the scraper.
#Is a mess, but I figured is not worth fixing if we're using a different method (API?).

import random
import string
import re
import urllib2
from bs4 import BeautifulSoup
import time
import urllib

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

base = "http://www.cdm.depaul.edu"

def get_Degrees():
    degrees = []

    #IS
    url = base + "/academics/Pages/MSInInformationSystems.aspx"
    soup = get_soup_from_url(url)
    ISConcentrations = []
    for li in soup.findAll("ul", { "class" : "sub-nav" })[0].findAll('li'):
        concentration = Concentration(li.a.text, li.a['href'], [])
        #print(li.a)
        ISConcentrations.append(concentration)
    degrees.append(Degree("MIS", soup.findAll("span", { "class" : "breadcrumbCurrent" })[0].text, ISConcentrations))

##    for x in ISConcentrations:
##        print(x.name)

    #CSC
    url = base + "/academics/Pages/MSInComputerScience.aspx"
    soup = get_soup_from_url(url)
    CSCConcentrations = []
    CSCConcentrations.append(Concentration("MS in Computer Science", "/academics/Pages/Current/Requirements-MS-in-Computer-Science.aspx", []))
    degrees.append(Degree("CSC", soup.findAll("span", {"class": "breadcrumbCurrent"})[0].text, CSCConcentrations))

##    for x in degrees:
##        print(x.name)

    return degrees

##def get_ISAnalysis():
##    degrees = []
##
##    #IS
##    url = base + "/academics/Pages/Current/Requirements-MS-IS-Business-Systems-Analysis.aspx"
##    soup = get_soup_from_url(url)
##    ISConcentrations = []
##    for tr in soup.findAll("table", { "class" : "courseList" })[0].findAll('tr'):
##        concentration = Concentration(tr.a.text, tr.a['href'])
##        ISConcentrations.append(concentration)
##    degrees.append(Degree("MIS", soup.findAll("span", { "class" : "breadcrumbCurrent" })[0].text, ISConcentrations))

def get_class_details(subject, nbr):
    

/html/body/div[3]/div/p[2]/text()

def get_soup_from_url(url):
    opener = urllib2.build_opener()
    url_opener = opener.open(url)
    page = url_opener.read()
    soup = BeautifulSoup(page, "html.parser")
    return soup

print(get_Degrees())

#get_ISAnalysis()
url = base + "/academics/Pages/Current/Requirements-MS-IS-Business-Systems-Analysis.aspx#"
soup = get_soup_from_url(url)
for tr in soup.findAll("table", { "class" : "courseList" })[0].findAll('tbody'):
    print(tr)

get_class_details('IS', '565'):
    
