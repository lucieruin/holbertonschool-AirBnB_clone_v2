#!/usr/bin/python3
""" starts a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_no_id():
    """ Defines a root for the root path for states without id """
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states_list', strict_slashes=False)
def states_id():
    """ Defines a root for the root path for states with id"""
    states = storage.all(State)
    for state in states:
        if storage.__class__.__name__ == 'DBStorage':
            state.cities = state.cities
        else:
            state.cities = storage.all(City).values()


@app.teardown_appcontext
def close(exception=None):
    """ Close DB after request """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
