import statistics

class SMA:
	def __init__(self):
		self.sma_5_arr = []
		self.sma_8_arr = []
		self.sma_13_arr = []
		self.sma_5 = 0
		self.sma_8 = 0
		self.sma_13 = 0

	def SMA_5(self, price):

		if len(self.sma_5_arr) > 4:
			self.sma_5_arr.pop(0)
		self.sma_5_arr.append(price)
		self.sma_5 = round(statistics.mean(self.sma_5_arr), 2)

	def SMA_8(self, price):

		if len(self.sma_8_arr) > 7:
			self.sma_8_arr.pop(0)
		self.sma_8_arr.append(price)
		self.sma_8 = round(statistics.mean(self.sma_8_arr), 2)
	
	def SMA_13(self, price):

		if len(self.sma_13_arr) > 12:
			self.sma_13_arr.pop(0)
		self.sma_13_arr.append(price)
		self.sma_13 = round(statistics.mean(self.sma_13_arr), 2)
