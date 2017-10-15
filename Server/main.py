from flask import Flask, request, Response
from datetime import datetime as dt
import datetime as d
import panda as pd
import io
import urllib2
import csv
import requests
import json
import psycopg2
from google import parseGoogle
from aylien import getArticleInfo

app = Flask(__name__)


TICKER_API_KEY = "hv8zy6k9mxehs-VxYB_k"

def connectToDB( query ):
	try:
		connect_str = "dbname='stockernews' user='stockernews' host='localhost' " + \
			  "password='stockernewspass'"
		# use our connection values to establish a connection
		conn = psycopg2.connect(connect_str)
		conn.autocommit = True
		# create a psycopg2 cursor that can execute queries
		cursor = conn.cursor()	
		cursor.execute(str( query ))
		return cursor.fetchall() 
	except Exception as e:
		print("Uh oh, can't connect. Invalid dbname, user or password? I am " + query[:3])
		print(e)

#Passes in an entity email. Gets PK to be used in other queries, also if doesnt exists created a row
def getOrCreateEntity(email):
	results = connectToDB("SELECT entity FROM tb_entity where email ilike'" + str(email) + ";")
	if len(results) == 0:
		connectToDB("INSERT INTO tb_entity VALUES( default, '" + email + "');")	
	results = connectToDB("SELECT entity FROM tb_entity where email ilike'" + str(email) + ";")
	return results[0][0];	
	
def addPortfolio(email, ticker):
	entity = getOrCreateEntity(email)
	tickerid = connectToDB("SELECT ticker FROM tb_ticker WHERE ticker_name ilike '" + str(ticker) + "';")
	connectToDB("INSERT INTO tb_portfolio values(default, " + str(entity) + "," + str(ticker_id) + ")")

def getPortfolio(email):
	entity = getOrCreateEntity(email)
	return connectToDB("SELECT t.ticker FROM tb_ticker t JOIN tb_portfolio p ON t.ticker = p.ticker WHERE p.entity = " + entity)[0]

# Get daily data on specific tickers. This will return data back to 2000 
def getTickerData(ticker):
	pardict = {'order':'asc', 'collapse': 'daily', 'start_date':'2016-01-01', 'end_date':'2017-10-13', 'api_key': TICKER_API_KEY, 'column_index':'4' }
	r = requests.get("https://www.quandl.com/api/v3/datasets/WIKI/" + ticker + ".csv", params = pardict)
	resp = Response(r)
	resp.headers['Access-Control-Allow-Origin'] = '*'
	return resp 

# Pass in the ticker and the amount you want in the API route. Will return stock market data for a ticker. 
# "short" for not a lot of data and "long" for a lot of data.
@app.route('/ticker', methods=['GET'])
def data():
        values = request.args.to_dict()
        ticker = values['ticker'].upper()
        return getTickerData(ticker);

#Ask for potfolio. Right now pass in email, wont need to pass in email after authentication.
@app.route('/portfolio', methods=['GET'])
def portfolio():
        values = request.args.to_dict()
        email = values['email']
        return getPortfolio(email);


#Get necessary news to pass to front-end
@app.route('/news', methods=['GET'])
def news():
        values = request.args.to_dict()
        ticker = values['ticker']
        date = values['date']
	
	pointDate = dt.fromtimestamp(int(date) / 1000).strftime('%m-%d-%Y')
	days_to_subtract = 7
	beforeDate = dt.strptime(pointDate, "%m-%d-%Y") - d.timedelta(days=days_to_subtract)
	afterDate = dt.strptime(pointDate, "%m-%d-%Y") + d.timedelta(days=days_to_subtract)

	articleInfo = getArticleInfo(parseGoogle(ticker, str(beforeDate), str(afterDate)))
	
	resp = Response(str(json.dumps(articleInfo)))
	resp.headers['Access-Control-Allow-Origin'] = '*'

        return resp

if __name__ == '__main__':
        app.run(host= '192.81.218.180', port=9000, debug=True, threaded=True)
