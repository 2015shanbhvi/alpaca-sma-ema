import config
import requests, json


class Account:
	def __init__(self):
		self.id = ""
		self.status = ""
		self.equity = ""
		self.buying_power = ""
		self.positions = {}

	#Input: None
	#Output: None
	#Action: assigns self.positions to a dict of all positions in account
	def getPositionsDict(self):
		r = requests.get(config.POSITIONS_URL, headers=config.HEADERS)
		response = json.loads(r.content)
		for position_obj in response:
			self.positions[position_obj["symbol"]] = position_obj["qty"]
		print("self.positions: ", self.positions) 

	#Input: None
	#Output: None
	#Action: Decides whether to make trade
	#def tradeDecision(self):