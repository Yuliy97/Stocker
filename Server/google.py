import requests
from urlparse import urlparse, parse_qs
from lxml.html import fromstring
from lxml.etree import tostring
from requests import get

#mm/dd/yyyy
#wsj, forbes, seekingalpha, investopedia, yahoo finance, fool, thestreet, cnn, foxnews
def parseGoogle(query, fromDate, toDate):
	newsLogic = "%20AND%20site%3Awww.wsj.com%20OR%20site%3Awww.forbes.com%20OR%20site%3Awww.seekingalpha.com%20OR%20site%3Awww.investopedia.com%20OR%20site%3Afinance.yahoo.com%20OR%20site%3Awww.fool.com%20OR%20site%3Awww.thestreet.com%20OR%20site%3Awww.cnn.com%20OR%20site%3Awww.foxnews"
	url = "https://www.google.com/search?q=" + query + newsLogic + "&source=lnt&tbs=cdr:1,cd_min:" + fromDate + ",cd_max:" + toDate + "&tbm="
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

	returnList = []
	r = requests.get(url,headers=headers)
	print r.url
	raw = r.text
	page = fromstring(raw)
	for result in page.cssselect(".r a"):
		hrefdata = result.get("href")
		returnList.append(hrefdata)
		#print hrefdata.tag
		#url = parse_qs(urlparse(url).query)['q']
	return returnList 



print parseGoogle("Microsoft", "12/10/1997", "12/10/2010")
