import requests
from aylienapiclient import textapi

APP_ID = "c7aa1f38" 
API_KEY = "1cee32948f87f4da56568c7c50395a15"

client = textapi.Client(APP_ID, API_KEY)

#Pass in article URL and recieve array of dictionaries with title, author, publishData, and url
def getArticleInfo(urls):
	responses = []
	for url in urls:
		extract = client.Extract({"url": url})
		responses.append({"author": extract["author"], "title":extract["title"], "publishDate":extract["publishDate"], "url": url})
 	return responses

