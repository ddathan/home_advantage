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


url = 'https://www.infogol.net/en/matches/result/english-premier-league/arsenal-vs-aston-villa-2020-11-08/70199'

options = Options()

driver = webdriver.Chrome('chromedriver_win32/chromedriver.exe',options=options)
driver.set_page_load_timeout(50)     
driver.get(url)
time.sleep(4)
element = driver.find_element_by_xpath('/html/body/div[1]/main/tf-match-details/div/match-shirts/div/div[3]/div/div/span[2]')

value = element.get_attribute("innerText")


driver.quit()




    
