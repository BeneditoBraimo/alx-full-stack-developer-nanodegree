"""
    Flask application that says 'Hello, world!'
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return "Hello, world!"

# if launched as a normal Python script

if __name__ == "__main__":
    app.run("0.0.0.0")