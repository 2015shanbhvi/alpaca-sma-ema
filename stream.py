import config
import websocket, json
from simplemovingaverage import SMA
from crossover import Crossover
from account import Account
from trade import Trade

#Callback method on open of websocket
def on_open(ws):
	print("opened websocket")
	auth_data = {
		"action": "authenticate",
		"data": {"key_id": config.API_KEY, "secret_key": config.SECRET_KEY}
	}

	ws.send(json.dumps(auth_data))

	listen_message = {"action": "listen", "data": {"streams": ["AM.AAPL"]}}

	ws.send(json.dumps(listen_message))

#Callback method on each received message in websocket
def on_message(ws, message):
	print("received a message")
	jmessage = json.loads(message)
	message_type = jmessage["stream"]
	#only print message if it is not an authorizxation or listening confirmation
	if not message_type == "authorization" and not message_type == "listening":
		
		account.getPositionsDict()

		data = jmessage["data"]
		closing_price = data["c"]

		#update SMAs
		print("current price AAPL: ", closing_price)
		sma5.add_to_SMA(closing_price)
		sma8.add_to_SMA(closing_price)
		sma13.add_to_SMA(closing_price)

		#calculate crossover
		if sma5.ready and sma8.ready and sma13.ready:
			crossover.calculateCrossover(sma5.sma, sma8.sma, sma13.sma, closing_price)
			if crossover.golden_cross:
				trade.create_order("AAPL", 1, "buy", "market", "gtc")
			elif crossover.death_cross:
				trade.create_order("AAPL", 1, "sell", "market", "gtc")
		else:
			print("SMAs not ready")


def on_error(ws, error):
    print(error)

def on_close(ws):
	print("closing websocket")




socket = "wss://data.alpaca.markets/stream"
sma5 = SMA(5) #create SMA object
sma8 = SMA(8)
sma13 = SMA(13)
crossover = Crossover() #to calculate crossover indicators
account = Account() #to list Account metadata
trade = Trade()  #to place orders
ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_error=on_error, on_close=on_close)
ws.run_forever()
#Vinays-MacBook-Pro-2:alpaca-sma-ema vinay.shanbhagibm.com$ python3 -m venv env
#Vinays-MacBook-Pro-2:alpaca-sma-ema vinay.shanbhagibm.com$ source env/bin/activate




