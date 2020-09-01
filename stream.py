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
		sma.SMA_5(closing_price)
		sma.SMA_8(closing_price)
		sma.SMA_13(closing_price)
		print(len(sma.sma_5_arr), " minute sma: ", sma.sma_5)
		print(len(sma.sma_8_arr), " minute sma: ", sma.sma_8)
		print(len(sma.sma_13_arr), " minute sma: ", sma.sma_13)

def on_error(ws, error):
    print(error)

def on_close(ws):
	print("closing websocket")

socket = "wss://data.alpaca.markets/stream"
sma = SMA() #create SMA object
account = Account()#create account object
ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_error=on_error, on_close=on_close)
ws.run_forever()
#{"action": "authenticate","data": {"key_id": "PKRLUBACQRIGHNSJ4C78", "secret_key": "WE4mAneR9hIgXc6eHkomUY2F3puRWSNrSb0WL1Az"}}





