#!flask/bin/python
#examples

from flask import Flask, jsonify, abort, make_response, request, url_for


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "Welcome"


if __name__ == '__main__':
    app.run(debug=True)



