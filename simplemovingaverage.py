import statistics

class SMA:
	def __init__(self, sma_num):
		self.sma_num = sma_num
		self.sma_arr = [0]*sma_num
		self.sma = 0
		self.pos = 0
		self.ready = False


	def add_to_SMA(self, price):

		#replacement strategy instead of pop and append
		if self.pos > self.sma_num - 1:
			self.ready = True
			self.pos = 0
		self.sma_arr[self.pos] = price
		self.pos += 1

		self.sma = round(statistics.mean(self.sma_arr), 2)

		
		if self.ready:
			print("The SMA", self.sma_num, " is ready:", self.sma)
	


#Inheritance
