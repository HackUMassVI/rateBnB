from flask import Flask, render_template, request
from flask_mako import MakoTemplates, render_template
import requests
import json

app = Flask(__name__)
mako = MakoTemplates(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.mako')
    else:
        form = request.form
        url = form.get('URL')
        origUrl = url
        temp = len(url)
        if "?" in url:
            temp = url.index("?")
        url = url[8:temp]
        returnedVal = "http://67.205.146.104:80/get_all_info?url=" + url
        r = requests.get(returnedVal)
        d = r.json()
        data = d[0]
        return scoreList(origUrl, data['amenities'], data['image'],data['listing_name'], data['rating'], data['review_count'], data['safety'], data['score'])
#, data['image'], data['listing_name'], data['rating'], data['review_count'], data['safety'], data['score']
#,image,listing_name,rating,review_count,safety,score,
@app.route('/scoreList', methods=['GET', 'POST'])
def scoreList(origUrl,amenities,image,listing_name,rating,review_count,safety,score):
        return render_template('scoredListing.mako', url=origUrl, amenities=amenities,image=image,listing_name=listing_name,rating=rating,review_count=review_count,safety=safety,score=score)

@app.route('/scoreListChrome')
def scoreListChrome():
    url = request.args.get('url')
    origUrl = url
    temp = len(url)
    if "?" in url:
        temp = url.index("?")
    url = url[8:temp]
    returnedVal = "http://67.205.146.104:80/get_all_info?url=" + url
    r = requests.get(returnedVal)
    d = r.json()
    data = d[0]
    return scoreList(origUrl, data['amenities'], data['image'],data['listing_name'], data['rating'], data['review_count'], data['safety'], data['score'])

@app.route('/about')
def about():
    return render_template('about.mako')


if __name__ == '__main__':
    app.run(debug=True)
