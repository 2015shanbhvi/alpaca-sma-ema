import statistics

class SMA:
	def __init__(self, sma_num):
		self.sma_num = sma_num
		self.sma_arr = []
		self.sma = 0


	def add_to_SMA(self, price):
		#manage the length
		if len(self.sma_arr) > self.sma_num - 1:
			self.sma_arr.pop(0)
		#add to it and recalculate average
		self.sma_arr.append(price)
		self.sma = round(statistics.mean(self.sma_arr), 2)

		#print value, or if not ready yet
		if len(self.sma_arr) < self.sma_num:
			print("SMA", self.sma_num, "has ", len(self.sma_arr), "datapoints and is not ready yet")
		else:
			print("SMA", self.sma_num, ": ", self.sma)

	