# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 16:13:53 2020

@author: dominicdathan
"""

import requests
from bs4 import BeautifulSoup

page = 'https://footystats.org/england/manchester-united-fc-vs-leicester-city-fc-h2h-stats#453873'

result = requests.get(page)

src = result.content

soup = BeautifulSoup(src,'lxml')

print(soup.prettify())

for div in soup.findAll('div', {'class': 'value'}):
    person[div.find('p').attrs['class'][0]] = div.text.strip()

print(person)