#from xmlutils.xml2csv import xml2csv
#import requests
#xml = requests.get("http://192.81.218.180:9000/ticker?ticker=AAPL").text
#
#file = open("xml.xml", "w")
#file.write(xml)
#file.close()
#
#
#converter = xml2csv("./xml.xml","./csv.csv",encoding="utf-8")
#num = converter.convert(tag="item")
#print num

import xml.etree.ElementTree as etree

child = etree.parse('./j.xml').getroot().find('child')

elements = ('Data', 'Open', 'High', 'Low', 'Close', 'Volume', 'Ex-Dividend', 'Split Ratio', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume')

for a in zip(*[child.findall(x) for x in elements]):
  print(", ".join([x.text for x in a]))
