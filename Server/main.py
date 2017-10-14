from flask import Flask, request
app = Flask(__name__)


@app.route('/ticker', methods=['GET'])
def data():
        values = request.args.to_dict()
        ticker = values['ticker']
        fromDate = values['fromDate']
        toDate = values['toDate']
        return str(ticker) + " " + str(fromDate) + " " + str(toDate)

if __name__ == '__main__':
        app.run(host= '192.81.218.180', port=9000, debug=False)
