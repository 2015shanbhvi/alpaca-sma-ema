import config
import websocket, json
#import obj.simplemovingaverage, obj.crossover, obj.account, obj.trade
from obj.simplemovingaverage import SMA
from obj.crossover import Crossover
from obj.account import Account
from obj.trade import Trade


class Stream:
	#Callback method on open of websocket
	def __init__(self):
		self.sma5 = SMA(5) #create SMA object
		self.sma8 = SMA(8)
		self.sma13 = SMA(13)
		self.crossover = Crossover() #to calculate crossover indicators
		self.account = Account() #to list Account metadata
		self.trade = Trade()  #to place orders


	def on_open(self, ws):
		print("opened websocket")
		auth_data = {
			"action": "authenticate",
			"data": {"key_id": config.API_KEY, "secret_key": config.SECRET_KEY}
		}

		ws.send(json.dumps(auth_data))

		listen_message = {"action": "listen", "data": {"streams": ["AM.AAPL"]}}

		ws.send(json.dumps(listen_message))

	#Callback method on each received message in websocket
	def on_message(self, ws, message):
		print("received a message")
		jmessage = json.loads(message)
		message_type = jmessage["stream"]
		#only print message if it is not an authorizxation or listening confirmation
		if not message_type == "authorization" and not message_type == "listening":

			data = jmessage["data"]
			closing_price = data["c"]

			#update SMAs
			print("current price AAPL: ", closing_price)
			self.sma5.add_to_SMA(closing_price)
			self.sma8.add_to_SMA(closing_price)
			self.sma13.add_to_SMA(closing_price)

			#calculate crossover and execute buy/sell if necessary
			if self.sma5.ready and self.sma8.ready and self.sma13.ready:
				self.crossover.crossoverTradeDecision(self.sma5, self.sma8, self.sma13, closing_price, self.account, self.trade)
			else:
				print("SMAs not ready")


	def on_error(self, ws, error):
	    print(error)

	def on_close(self, ws):
		print("closing websocket")

	#Contains the websocket
	#and instantiates Crossover, Account, SMA, and Trade objects
	def start(self):
		socket = "wss://data.alpaca.markets/stream"
		ws = websocket.WebSocketApp(socket, on_open=self.on_open, on_message=self.on_message, on_error=self.on_error, on_close=self.on_close)
		ws.run_forever()
		#Vinays-MacBook-Pro-2:alpaca-sma-ema vinay.shanbhagibm.com$ python3 -m venv env
		#Vinays-MacBook-Pro-2:alpaca-sma-ema vinay.shanbhagibm.com$ source env/bin/activate




