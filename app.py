from stream import Stream
from threading import Thread
from flask import Flask, request
from flask_restful import Api
from flask_jsonpify import jsonify
import sys, logging

app = Flask(__name__)
api = Api(app)

stream = Stream()

@app.route('/')
def hello():
	if not stream.started:
		stream.started = True
		Thread(target = stream.start).start()
	return "Started stream in hello()"

@app.route('/getHistory')
def get(): 
	return "this is getHistory"
	# stream.account.fillPositionsDict()
	# return jsonify(stream.account.positions)


def main():
	print("********************************")
	print("Welcome to my Alpaca trading bot")
	print("********************************")
	
	# stream()
	# app.run(port='8080')
	#stream = Stream()
	Thread(target = stream.start).start()
	Thread(target = app.run(port='8080')).start()

	

if __name__ == "__main__":
	app.run(host='0.0.0.0', port='8080', debug=True)
	#main()

