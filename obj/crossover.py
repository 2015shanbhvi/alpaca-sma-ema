
class Crossover:
	def __init__(self):
		self.short_trend = 0
		self.long_trend = 0
		self.golden_cross = False
		self.death_cross = False
		self.ready = False



	#takes in sma5, sma8, sma13, current price
	#updates class variables golden_cross and death_cross
	def calculateCrossover(self, sma5, sma8, sma13, current_price):
		#if trends are valid
		shorter = round((sma5+current_price)/2,2)
		longer = round((sma8+sma13)/2, 2)

		if self.short_trend and self.long_trend:
			self.ready = True

			uptrend = True if self.short_trend > self.long_trend else False
			shorter = round((sma5+current_price)/2,2)
			longer = round((sma8+sma13)/2, 2)

			#then if short_trend is lower than long_trend,
			#means downtrend previously
			#but sma5+current_price is greater than sma8+sma13, then
			#we set golden_cross to True
			if not uptrend and shorter > longer:
				print("golden cross TRUE")
				self.golden_cross = True
				self.death_cross = False


			#if if short_trend is higher than long_trend
			#means uptrend previously
			#but sma5+current_price is lower than sma8+sma13,
			#then we set golden_cross to False
			elif uptrend and shorter < longer:
				print("death cross TRUE")
				self.golden_cross = False
				self.death_cross = True

			else:
				print("no crossover")
				self.golden_cross = False
				self.death_cross = False

		#update short and long trends 
		self.short_trend = shorter
		self.long_trend = longer




	def crossoverTradeDecision(self, sma5, sma8, sma13, closing_price, account, trade):
		self.calculateCrossover(sma5.sma, sma8.sma, sma13.sma, closing_price)
		if account.getShareEligibility("AAPL", 5):
			if self.golden_cross:
				print("Buying one share of AAPL")
				trade.create_order("AAPL", 1, "buy", "market", "gtc")
				print(account.getPositionsDict())
			elif self.death_cross:
				print("Selling one share of AAPL")
				trade.create_order("AAPL", 1, "sell", "market", "gtc")
				print(account.getPositionsDict())

