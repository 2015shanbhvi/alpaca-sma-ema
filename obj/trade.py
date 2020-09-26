import requests, json
import alpaca_trade_api as tradeapi
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# import ../db.py
import config

class Trade:

	### Set Up Methods ###
	def get_account(self):
		response = requests.get(config.ACCOUNT_URL, headers=config.HEADERS)
		return json.loads(response.content)

	def getAccountSummary(self):
		response = requests.get(config.ACCOUNT_URL, headers=config.HEADERS)
		responseJSON = response.json()
		print("STATUS: ", responseJSON["status"])
		print("Equity: ", addCommas(responseJSON["equity"]))
		print("Buying Power: ", addCommas(responseJSON["buying_power"]))

	def addCommas(self, amount):
		new_amount = amount.split('.')[0]
		number_with_commas = "{:,}".format(int(new_amount))
		return number_with_commas

	#response = create_order("AAPL", 100, "buy", "market", "gtc")
	def create_order(self, symbol, qty, side, type, time_in_force):
		data = {
			"symbol": symbol,
			"qty": qty,
			"side": side,
			"type": type,
			"time_in_force": time_in_force,
		}
		r = requests.post(config.ORDERS_URL, json=data, headers=config.HEADERS)
		return json.loads(r.content)

	#Get market data:
	def getBars(self):
		api = tradeapi.REST(API_KEY, SECRET_KEY, base_url=config.BASE_URL)
		account = api.get_account()
		barset = api.get_barset('AAPL', 'minute', 1)
		aapl_barset = barset["AAPL"]
		print("aapl_barset: ", aapl_barset)


#create_order("AAPL", 1, "buy", "market", "gtc")



