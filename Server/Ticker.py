import pandas as pd
import requests
import http.client, urllib.parse, json

key = "AIzaSyDizFCUNdx2Dy4ec4EZFK-45e22IEiZyms"
cx = "014648043321448172607:xdflm89oewm"

# subscriptionKey = "00d189f582da443a94e3cc94be36780b"


stocks = pd.read_csv("/Users/justinduan/Documents/HackGT/stocklist.csv")

tick = "MSFT"

len(stocks[["Symbol"]])

company = ""
low = "20151201"
high = "20161201"

for i in range(len(stocks["Symbol"])):
	if stocks["Symbol"][i] == tick:
		company = stocks["Name"][i]

# host = "api.cognitive.microsoft.com"
# path = "/bing/v5.0/news/search"

# term = company

# def BingNewsSearch(search):
# 	headers = {'Ocp-Apim-Subscription-Key': subscriptionKey}
# 	conn = http.client.HTTPSConnection(host)
# 	query = urllib.parse.quote(search)
# 	conn.request("GET", path + "?q=" + query, headers=headers, params=parameters)
# 	response = conn.getresponse()
# 	# headers = [k + ": " + v for (k, v) in response.getheaders()
# 	# if k.startswith("BingAPIs-") or k.startswith("X-MSEdge-")]
# 	# return headers, response.read().decode("utf8")
# 	return response.read().decode("utf8")

# response = BingNewsSearch(term)
# result = json.loads(response)

# lst = result.get('value')[0].items()
# print(lst)
# # for x in headers:
# # 	lst.append(headers)
# print(result.get('value')[0].keys())

# print("\nRelevant HTTP Headers:\n")
# print("\n".join(headers))
# print("\nJSON Response:\n")
# print(json.dumps(json.loads(result), indent=4))

url = "https://www.googleapis.com/customsearch/v1"
parameters = {"q": company + "news",
              "cx": cx,
              "key": key,
              "dateRestrict": "y[2]",
              "lowRange":low,
              "highRange": high
              }
page = requests.request("GET", url, params=parameters)
results = json.loads(page.text)

links = []

for x in results['items']:
	links.append(x.get('link'))

for y in links:
	print(y)
