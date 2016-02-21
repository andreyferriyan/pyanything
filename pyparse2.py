#!/usr/bin/env python
# Web Parsing Script
# Author : Andrey Ferriyan
# Script : pyparse2.py
# This script will extract all parameter from this site www.cpcb.gov.in 
# and then show to the command line.

from bs4 import BeautifulSoup as bs
import urllib.request

url = """
http://www.cpcb.gov.in/CAAQM/frmCurrentDataNew.aspx?CityId=7&StationName=Hyderabad&StateId=30
"""

f = urllib.request.urlopen(url)
content = f.read()
f.close()
parsing_content = bs(content, "html.parser")

table = parsing_content.find('td', attrs={'id': 'Td1'})
print(table.findAll('td')[7].get_text())
counter = 7
for link in range(len(table.findAll('td'))):
    try:
        counter = counter + 7
        print(table.findAll('td')[counter].get_text())
    except IndexError:
        exit()
