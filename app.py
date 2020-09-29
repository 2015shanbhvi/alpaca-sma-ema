from stream import *
from threading import Thread
from flask import Flask, request
from flask_restful import Api
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)


@app.route('/')
def hello():
   return "Welcome to the Alpaca trade bot"

@app.route('/getHistory')
def get(): 
	retval = "GET request from class History"
	return jsonify(retval)


def main():
	print("********************************")
	print("Welcome to my Alpaca trading bot")
	print("********************************")
	
	# stream()
	# app.run(port='8080')
	stream = Stream()
	Thread(target = stream.start).start()
	Thread(target = app.run(port='8080')).start()

	

if __name__ == "__main__":
    main()

