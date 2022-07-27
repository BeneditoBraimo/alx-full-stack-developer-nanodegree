from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('__name__')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres@localhost:5432/example'
db = SQLAlchemy(app)

# class to be mapped to the database
class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)


@app.route('/')

def index():
    return "Hello, world!"


if __name__ == "__main__":
    app.run("0.0.0.0")

# enable debug mode on run
if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=3000)