"""
    Flask application that says 'Hello, world!'
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return "Hello, world!"