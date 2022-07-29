from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:abc@localhost:5432/example2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"<User ID: {self.id}, user name: {self.name}>"

db.create_all()


if __name__ == "__main__":
    app.debug = True
    app.run("0.0.0.0", port=3000)