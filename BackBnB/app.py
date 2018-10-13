#!flask/bin/python
#examples

from flask import Flask, jsonify, abort, make_response, request, url_for
import urllib.request as urllib2
from bs4 import BeautifulSoup
import html2text
from ast import literal_eval

app = Flask(__name__)


def get_page(link):
    try:
        if link.find('mailto') != -1:
            return ''
        req = urllib2.Request(link, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'})
        html = urllib2.urlopen(req).read()
        html = BeautifulSoup(html,"html.parser")
        return html
    except (urllib2.URLError, urllib2.HTTPError, ValueError) as e:
        return 'error getting airBnB page'

def get_coords(page):
    index = page.index(b"listing_lat")
    coord_str = page[index-1:index+63].decode("utf-8")
    coord_dict = literal_eval(literal_eval("{"+coord_str+"}"))
    return str(coord_str['listing_lat']), str(coord_str['listing_lng'])

@app.route('/', methods=['GET'])
def home():
    return "Welcome"

@app.route('/get_rating', methods=['GET'])
    # error handling
    if not request.values:
        abort(400)
    url = request.values['url']
    page = get_page(url)
    lat,lon = get_coords(page)
    crime_index = get_crime_index(lat,lon)

    return crime_index


if __name__ == '__main__':
    app.run(debug=True)



