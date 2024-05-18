#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """displays Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displays HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """displays C <text>"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """displays Python <text>"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:number>', strict_slashes=False)
def number(number):
    """displays number"""
    return str(number) + ' is a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
