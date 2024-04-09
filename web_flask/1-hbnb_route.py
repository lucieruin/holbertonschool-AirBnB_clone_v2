#!/usr/bin/python3
""" starts a Flask web application with 2 routes"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Defines a root for the root path """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Defines a root for the root path """
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
