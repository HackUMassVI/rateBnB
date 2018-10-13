#!flask/bin/python
#examples

from flask import Flask, jsonify, abort, make_response, request, url_for
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
	return "Welcome"


def getCrimeIndex(lat,lon):
	url = "https://crimescore.p.mashape.com/crimescore?f=json&id=174&lat=" + lat + "&lon=" + lon
	headers = {"X-Mashape-Key": "qWMc2K59dgmshJH33sKjN5KILREOp1QQXj2jsniuCdIgcwNvTi", "Accept": "application/json"}
	response = requests.get(url, headers = headers)
	crime_dict = json.loads(response.text)
	return crime_dict["score"]

if __name__ == '__main__':
    app.run(debug=True)



