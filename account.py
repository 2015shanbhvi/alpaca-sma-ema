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
			self.positions[position_obj["symbol"]] = int(position_obj["qty"])
		print("self.positions: ", self.positions) 

	#make sure we are at a range of [1, threshold-1] number of shares
	#in order for us to be able to buy or sell one share
	def getShareEligibility(self, symbol, threshold):
		if self.positions[symbol] >= threshold or self.positions[symbol] < 1:
			return False
		return True