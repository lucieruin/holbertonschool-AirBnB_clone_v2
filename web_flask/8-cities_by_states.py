#!/usr/bin/python3
""" starts a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Defines a root for the root path for states """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Defines a root for the root path for cities """
    states = storage.all(State)
    return render_template('/8-cities_by_states.html', states=states)


@app.teardown_appcontext
def close(self):
    """ close DB after request """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)