import config
import requests, json


class Account:
	def __init__(self):
		self.positions = {}

	#Input: None
	#Output: None
	#Action: assigns self.positions to a dict of all positions in account
	def fillPositionsDict(self):
		r = requests.get(config.POSITIONS_URL, headers=config.HEADERS)
		response = json.loads(r.content)
		for position_obj in response:
			self.positions[position_obj["symbol"]] = int(position_obj["qty"])

	#make sure we are at a range of [1, threshold-1] number of shares
	#in order for us to be able to buy or sell one share
	def getNumShares(self, symbol):
		self.fillPositionsDict() #populate the dict first
		if symbol in self.positions.keys():
			return self.positions["symbol"]
		return 0
		