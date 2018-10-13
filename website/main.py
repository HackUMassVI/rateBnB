from flask import Flask, render_template, request
from flask_mako import MakoTemplates, render_template
import requests


app = Flask(__name__)
mako = MakoTemplates(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.mako')
    else:
        form = request.form
        url = form.get('URL')
        url = url[8:]
        returnedVal = "http://127.0.0.1:80/get_rating?url=" + url
        r = requests.get(returnedVal)
        return scoreList(r.text)

@app.route('/scoreList', methods=['GET', 'POST'])
def scoreList(returnedVal):
        return render_template('scoredListing.mako', response=returnedVal)

@app.route('/about')
def about():
    return render_template('about.mako')


if __name__ == '__main__':
    app.run(debug=True)