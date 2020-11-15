# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 17:35:33 2020

@author: ddath
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import re
import time
from   pandas import read_html
import random
import json
from io import StringIO
from datetime import datetime, timedelta
from itertools import islice
import numpy as np
from datetime import date
import datetime
import os

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def get_result(driver,options,url):

    driver.get(url)
    time.sleep(4)
    
    # get teams 
    element = driver.find_element_by_xpath('/html/body/div[1]/main/tf-match-details/div/match-shirts/div/div[1]/div[1]/a')
    home_team = element.get_attribute("innerText")
    element = driver.find_element_by_xpath('/html/body/div[1]/main/tf-match-details/div/match-shirts/div/div[1]/div[3]/a')
    away_team = element.get_attribute("innerText")
    # get scores
    element = driver.find_element_by_xpath('/html/body/div[1]/main/tf-match-details/div/match-shirts/div/div[1]/div[2]')
    strscores = element.get_attribute("innerText")
    scores = strscores.split('-')
    scores = [int(x.strip()) for x in scores]
    
    # get xgs
    element = driver.find_element_by_xpath('/html/body/div[1]/main/tf-match-details/div/match-shirts/div/div[3]/div/div/span[2]')
    # get text of xgs for both teams
    strxgs = element.get_attribute("innerText")
    # split xgs
    xgs = strxgs.split('-')
    # remove white space and convert to float
    xgs =  [float(x.strip()) for x in xgs]
    
    match = {'Home Team': home_team,
             'Home Team Goals': scores[0],
             'Home Team Xg': xgs[0],
             'Away Team': away_team,
             'Away Team Goals': scores[1],
             'Away Team Xg': xgs[1]}
    
    df = pd.DataFrame.from_dict(match,orient='index').transpose()
    
    return df



options = Options()

driver = webdriver.Chrome('chromedriver_win32/chromedriver.exe',options=options)
driver.set_page_load_timeout(50) 

url = 'https://www.infogol.net/en/matches/results/2020-11-07'
driver.get(url)
#comps = driver.find_elements_by_class_name('competition-header-name.ng-binding')
#<td class="match-text match-time match-fulltime" ng-click="$ctrl.openMatch($event)" ng-class="$ctrl.getStatusClass()"><span class="ng-binding">FT<span class="icon icon-chevron-right"></span></span></td>

#comps = driver.find_elements_by_class_name("competition-header")
comps = driver.find_elements_by_xpath("/html/body/div[1]/main/section/tf-match-list/div/ul/li[1]")
for element in comps:
    # get competition
    comp = element.find_elements_by_class_name("competition-header")[0]
    #print(element.get_attribute("innerText"))
    if comp.get_attribute("innerText") == "English Premier League":
        print(element.get_attribute("outerText"))
        matches = element.find_elements_by_xpath("/html/body/div[1]/main/section/tf-match-list/div/ul/li[1]/ul/li[1]/match-header/div")
        for match in matches:
            # NEED TO WORK OUT HOW TO GET URLS TO EACH MATCH
            ftlink = match.find_element_by_class("match-text match-time match-fulltime")
            print(ftlink.get_attribute("href"))
            #match.click()
        break
     

url = 'https://www.infogol.net/en/matches/result/english-premier-league/arsenal-vs-aston-villa-2020-11-08/70199'

#df = get_result(driver,options,url)

driver.quit()


    
