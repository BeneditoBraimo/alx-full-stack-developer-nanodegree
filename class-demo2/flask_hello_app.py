from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('__name__')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:abc@localhost:5432/example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# class to be mapped to the database
class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

# create database models
db.create_all()
@app.route('/')

def index():
    person = Person.query.first()
    return "Hello, " + person.name


if __name__ == "__main__":
    app.run("0.0.0.0")

# enable debug mode on run
if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=3000)