#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask
from flask import render_template
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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """display a HTML page only if n is an integer"""
    if n % 2 == 0:
        even = "even"
    else:
        even = "odd"
    return render_template('6-number_odd_or_even.html', n=n, even=even)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
