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
    def __init__(self, name, link):
        self.name = name
        self.link = link

class Class:
    def __init__(self, c, n, p):
        self.code = c
        self.name = n
        self.prereqs = p

class Sections:
    def __init__(self, c, n, u,d):
        self.code = c
        
        self.name = n
        self.url = u
        self.dept = d

base = "http://www.cdm.depaul.edu"

def get_Degrees():
    degrees = []

    #IS
    url = base + "/academics/Pages/MSInInformationSystems.aspx"
    soup = get_soup_from_url(url)
    ISConcentrations = []
    for li in soup.findAll("ul", { "class" : "sub-nav" })[0].findAll('li'):
        concentration = Concentration(li.a.text, li.a['href'])
        ISConcentrations.append(concentration)
    degrees.append(Degree("MIS", soup.findAll("span", { "class" : "breadcrumbCurrent" })[0].text, ISConcentrations))

    #CSC
    url = base + "/academics/Pages/MSInComputerScience.aspx"
    soup = get_soup_from_url(url)
    CSCConcentrations = []
    CSCConcentrations.append(Concentration("MS in Computer Science", "/academics/Pages/Current/Requirements-MS-in-Computer-Science.aspx"))
    degrees.append(Degree("CSC", soup.findAll("span", {"class": "breadcrumbCurrent"})[0].text, CSCConcentrations))
    return degrees

def get_soup_from_url(url):
    opener = urllib2.build_opener()
    url_opener = opener.open(url)
    page = url_opener.read()
    soup = BeautifulSoup(page, "html.parser")
    return soup
    


print(get_Degrees())
