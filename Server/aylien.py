import requests
from aylienapiclient import textapi

APP_ID = "c7aa1f38" 
API_KEY = "1cee32948f87f4da56568c7c50395a15"

client = textapi.Client(APP_ID, API_KEY)

urls = ['http://www.wsj.com/articles/SB108662728298030562', 'http://www.investopedia.com/ask/answers/120314/who-are-microsofts-msft-main-competitors.asp', 'https://www.forbes.com/2005/12/23/gates-microsoft-google-cx_cn_1223autofacescan02.html', 'https://www.forbes.com/2007/02/14/microsoft-lawsuit-settlement-tech-cz_dl_0214lawsuit.html', 'https://www.fool.com/investing/small-cap/2004/10/22/microsoft-and-unearned-revenue.aspx', 'http://www.cnn.com/TECH/computing/9811/18/msknows.cdx.idg/', 'http://www.investopedia.com/financial-edge/0712/microsoft-vs.-apple.aspx', 'https://www.forbes.com/2008/03/11/microsoft-hoover-regulate-oped-cx_fsk_0311microsoft.html', 'http://www.investopedia.com/ask/answers/08/microsoft-antitrust.asp', 'http://www.wsj.com/articles/SB123207131111388507'] 
#Pass in article URL and recieve title
def getTitle(url):
	for url in urls:
		extract = client.Extract({"url": url})
		sentiment = client.Sentiment({"text": extract["title"]})
		return str(extract['title'])
