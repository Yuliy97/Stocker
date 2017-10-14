from flask import Flask, request
import requests
app = Flask(__name__)

TICKER_API_KEY = 'EGOES1RF7XCEQB6U'

# Get daily data on specific tickers. This will return data back to 5 months
def getTickerDailyDataShort(ticker):
	r = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + str(ticker) + "&apikey=" + TICKER_API_KEY)
	return r.content

# Get daily data on specific tickers. This will return data back to 17 years or more. Takes a while to get all the data 
def getTickerDailyDataLong(ticker):
	r = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol=" + str(ticker) + "&apikey=" + TICKER_API_KEY)
	return r.content


# Pass in the ticker and the amount you want in the API route. Will return stock market data for a ticker. 
# "short" for not a lot of data and "long" for a lot of data.
@app.route('/ticker', methods=['GET'])
def data():
        values = request.args.to_dict()
        ticker = values['ticker']
        amount = values['amount']
        if amount == "short":
		results = getTickerDailyDataShort(ticker)
	elif amount == "long":
		results = getTickerDailyDataLong(ticker);
        return results

if __name__ == '__main__':
        app.run(host= '192.81.218.180', port=9000, debug=True)
