from flask import Flask, render_template
from flask_mako import MakoTemplates, render_template

app = Flask(__name__)
mako = MakoTemplates(app)

@app.route('/')
def home():
    return render_template('index.mako')

@app.route('/about')
def about():
    return render_template('about.mako')
