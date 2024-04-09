#!/usr/bin/python3
""" starts a Flask web application with 2 routes"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Defines a root for the root path """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Defines a root for the root path /hbnb """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C_is_fun(text):
    """ Defines a root for the root path /c """
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
def Python_is_fun(text):
    """ Defines a root for the root path "/python" """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def Integer_only(n):
    """ Defines a root for the root path "/number" """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ Defines a root for the root path with template """
    return render_template('5-number.html', number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def Odd_or_even(n):
    """ Defines a root with template if odd or even """
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
