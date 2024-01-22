'''this module contains a script that creates web application using flask'''

    
'''importing flask'''
from flask import Flask

'''creates the variable application name'''
app = Flask(__name__)

'''route for retrieving hello HBNB'''
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return 'C ' + text.replace('_', ' ')

@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python_text(text='is cool'):
    return 'Python ' + text.replace('_', ' ')

@app.route('/number/<n>', strict_slashes=False)
@app.route('/number/', strict_slashes=False)
def number(n):
    try:
        type(n) == int
        return '{} is a number'.format(n)
    except ValueError:
        return 404
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
