#!/usr/bin/python3
""" starts a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_no_id():
    """ Defines a root for the root path for states without id """
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """ Defines a root for the root path for states with id"""
    states = storage.all(State)
    state_id = "State." + id if id else None
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def close(self):
    """ Close DB after request """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
