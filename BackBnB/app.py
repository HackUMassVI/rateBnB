#!flask/bin/python
#examples

from flask import Flask, jsonify, abort, make_response, request, url_for
import urllib.request as urllib2
from bs4 import BeautifulSoup
import html2text
from ast import literal_eval
import requests
import json

app = Flask(__name__)


def get_page(link):
	try:
		if link.find('mailto') != -1:
			return ''
		req = urllib2.Request(link, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'})
		html = urllib2.urlopen(req).read()
		return html
	except (urllib2.URLError, urllib2.HTTPError, ValueError) as e:
		return 'error getting airBnB page'

def get_coords(page):
	index = page.index(b"listing_lat")
	coord_str = page[index-1:index+63].decode("utf-8")
	coord_str = "{"+coord_str+"}".replace("'","\"")
	coord_dict = json.loads(coord_str)
	return str(coord_dict['listing_lat']), str(coord_dict['listing_lng'])

def get_crime_index(lat,lon):
	url = "https://crimescore.p.mashape.com/crimescore?f=json&id=174&lat=" + lat + "&lon=" + lon
	headers = {"X-Mashape-Key": "qWMc2K59dgmshJH33sKjN5KILREOp1QQXj2jsniuCdIgcwNvTi", "Accept": "application/json"}
	response = requests.get(url, headers = headers)
	crime_dict = json.loads(response.text)
	return crime_dict['score']

@app.route('/get_rating', methods=['GET'])
def get_index():
	url = str(request.values['url'])
	url = "https://"+url
	page = get_page(url)
	return page
	lat,lon = get_coords(page)
	crime_index = get_crime_index(lat,lon)



if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=80)
