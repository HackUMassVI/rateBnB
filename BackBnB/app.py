#!flask/bin/python

from flask import Flask, jsonify, abort, make_response, request, url_for, jsonify
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

def get_listing_name(page):
	search_str = "<title>"
	page = page.decode("utf-8")
	index = page.index(search_str)
	first = page[index+len(search_str):]
	last = first.index("</title>")
	listing_name = first[:int(last)]
	return listing_name

def get_image(page):
	search_str = "rel=\"image_src\" href=\""
	page = page.decode("utf-8")
	index = page.index(search_str)
	first = page[index+len(search_str):]
	last = first.index("\">")
	img_src = first[:int(last)]
	return img_src

def get_rating(page):
	search_str = " out of 5"
	page = page.decode("utf-8")
	try:
		index = page.index(search_str)
	except:
		return 0
	return page[index-1]
	
def get_review_count(page):
	search_str = "reviewCount"
	page = page.decode("utf-8")
	try:
		index = page.index(search_str)
	except:
		return 0
	short = page[index:]
	first = short.index("content=")
	l = len("content=\"")
	return short[first+l:short.index("\">")]

def get_amenities(page):
	amenities = ['Wifi', 'Kitchen', 'Free street parking', 'Air conditioning', 'Laptop friendly workspace', 'Cable TV', 'Hangers']
	page = page.decode("utf-8")
	available = []
	for a in amenities:
		if page.find(a) !=-1:
			available.append(a)
	return available

def get_score(review_count, rating, amenities, safety):
	# 50% crime, 20% review_count 20% rating 10% amenties
	review_c = 100 if int(review_count)>=100 else int(review_count)
	score = float(safety)/100.0*0.3 + (float(len(amenities))/7.0)*0.2 + (float(rating)/5.0)*0.3 + (float(review_c)/100.0)*0.2
	return str("{0:.2f}".format(score*100))+"%"

def get_crime_index(lat,lon):
	url = "https://crimescore.p.mashape.com/crimescore?f=json&id=174&lat=" + lat + "&lon=" + lon
	headers = {"X-Mashape-Key": "qWMc2K59dgmshJH33sKjN5KILREOp1QQXj2jsniuCdIgcwNvTi", "Accept": "application/json"}
	response = requests.get(url, headers = headers)
	crime_dict = json.loads(response.text)
	return crime_dict['score']

@app.route('/', methods=['GET'])
def home():
	return "Hello, welcome to the backend of rateBnB"

@app.route('/get_all_info', methods=['GET'])
def get_index():
	url = str(request.values['url'])
	url = "https://"+url
	page = get_page(url)
	lat,lon = get_coords(page)
	crime_index = get_crime_index(lat,lon)
	listing_name = get_listing_name(page)
	img_src = get_image(page)
	rating = get_rating(page)
	review_count = get_review_count(page)
	amenities = get_amenities(page)
	score = get_score(review_count, rating, amenities, crime_index)
	output = [{
				'listing_name':listing_name, 
				'image':img_src,
				'rating':rating,
				'review_count':review_count,
				'safety':crime_index,
				'amenities':amenities,
				'score':score
	}]
	return jsonify(output)

@app.route('/chrome_get', methods=['GET'])
def get_chrome():
	url = str(request.values['url'])
	url = "https://"+url
	page = get_page(url)
	lat,lon = get_coords(page)
	crime_index = get_crime_index(lat,lon)
	listing_name = get_listing_name(page)
	img_src = get_image(page)
	rating = get_rating(page)
	review_count = get_review_count(page)
	amenities = get_amenities(page)
	score = get_score(review_count, rating, amenities, crime_index)
	return score[:2]

@app.route('/ios_get', methods=['GET'])
def get_ios():
	url = str(request.values['url'])
	url = "https://"+url
	page = get_page(url)
	lat,lon = get_coords(page)
	crime_index = get_crime_index(lat,lon)
	listing_name = get_listing_name(page)
	img_src = get_image(page)
	rating = get_rating(page)
	review_count = get_review_count(page)
	amenities = get_amenities(page)
	score = get_score(review_count, rating, amenities, crime_index)
	output = {
				'listing_name':listing_name, 
				'image':img_src,
				'rating':rating,
				'review_count':review_count,
				'safety':crime_index,
				'amenities':amenities,
				'score':score
	}
	return jsonify(output)

@app.route('/android_get', methods=['GET'])
def get_android():
	url = str(request.values['url'])
	url = "https://"+url
	page = get_page(url)
	lat,lon = get_coords(page)
	crime_index = get_crime_index(lat,lon)
	listing_name = get_listing_name(page)
	img_src = get_image(page)
	rating = get_rating(page)
	review_count = get_review_count(page)
	amenities = get_amenities(page)
	score = get_score(review_count, rating, amenities, crime_index)
	output = {
				'listing_name':listing_name, 
				'image':img_src,
				'rating':rating,
				'review_count':review_count,
				'safety':crime_index,
				'amenities':amenities,
				'score':score
	}
	return json.dumps(output)


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=80)
