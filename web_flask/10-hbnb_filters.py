#!/usr/bin/python3
"""
start Flask application
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """
    display a HTML page with states and cities listed alphabetically
    """
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """
    A function to close the SQLAlchemy Session at the end of the request

    Args:
        exception (Exception): An exception raised by an application

    Returns:
        None
    """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
