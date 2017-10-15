#!/usr/bin/python
import requests
import csv
from urlparse import urlparse, parse_qs
from lxml.html import fromstring
from lxml.etree import tostring
from requests import get
import panda as pd

#mm/dd/yyyy
#wsj, forbes, seekingalpha, investopedia, yahoo finance, fool, thestreet, cnn, foxnews
def parseGoogle(tick, fromDate, toDate):
	query = ""
	with open("./stocklist.csv", 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			if row[0] == tick:
				query = row[1]
				break


	newsLogic = "%20AND%20site%3Awww.wsj.com%20OR%20site%3Awww.forbes.com%20OR%20site%3Awww.seekingalpha.com%20OR%20site%3Awww.investopedia.com%20OR%20site%3Afinance.yahoo.com%20OR%20site%3Awww.fool.com%20OR%20site%3Awww.thestreet.com%20OR%20site%3Awww.cnn.com%20OR%20site%3Awww.foxnews"
	url = "https://www.google.com/search?q=" + query + newsLogic + "&source=lnt&tbs=cdr:1,cd_min:" + fromDate + ",cd_max:" + toDate + "&tbm="
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

	returnList = []
	r = requests.get(url,headers=headers)
	raw = r.text
	page = fromstring(raw)
	for result in page.cssselect(".r a"):
		hrefdata = result.get("href")
		returnList.append(hrefdata)
		#print hrefdata.tag
		#url = parse_qs(urlparse(url).query)['q']
	if len(returnList) > 5:
		returnList = returnList[:5]
	return returnList 


