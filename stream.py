import config
import websocket, json
from simplemovingaverage import SMA
from account import Account

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

		sma5.add_to_SMA(closing_price)
		sma8.add_to_SMA(closing_price)
		sma13.add_to_SMA(closing_price)

		# sma.add_SMA_5(closing_price)
		# sma.add_SMA_8(closing_price)
		# sma.add_SMA_13(closing_price)



def on_error(ws, error):
    print(error)

def on_close(ws):
	print("closing websocket")

socket = "wss://data.alpaca.markets/stream"
sma5 = SMA(5) #create SMA object
sma8 = SMA(8)
sma13 = SMA(13)
account = Account()#create account object
ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_error=on_error, on_close=on_close)
ws.run_forever()
#Vinays-MacBook-Pro-2:alpaca-sma-ema vinay.shanbhagibm.com$ python3 -m venv env
#Vinays-MacBook-Pro-2:alpaca-sma-ema vinay.shanbhagibm.com$ source env/bin/activate




