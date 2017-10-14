from flask import Flask, request
import requests
import psycopg2

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
	pardict = {'collapse': 'daily', 'start_date':'2000-01-01', 'end_date':'2017-10-13', 'api_key': TICKER_API_KEY }
	r = requests.get("https://www.quandl.com/api/v3/datasets/WIKI/" + ticker + ".xml", params = pardict)
	return r.content


# Pass in the ticker and the amount you want in the API route. Will return stock market data for a ticker. 
# "short" for not a lot of data and "long" for a lot of data.
@app.route('/ticker', methods=['GET'])
def data():
        values = request.args.to_dict()
        ticker = values['ticker'].upper()
        return getTickerData(ticker);


#Get necessary news to pass to front-end
@app.route('/news', methods=['GET'])
def news():
        values = request.args.to_dict()
        ticker = values['ticker']
        fromDate = values['fromDate']
#	call Justin's function
#	call Justin's function
#	call Justin's function
        return "Got you the news!"

if __name__ == '__main__':
        app.run(host= '192.81.218.180', port=9000, debug=True)
