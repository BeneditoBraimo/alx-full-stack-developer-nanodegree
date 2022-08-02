from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:abc@localhost:5432/todoapp"
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

db = SQLAlchemy(app)

class Todos(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(), nullable=False)

    def __rep__(self):
        return f"<ID: {self.id}, description {self.description}>"

    
@app.route("/")
def index():
    return render_template("index.html", data=[
        {
            "description": "Todo 1"
        },

        {
            "description": "Todo 2"
        },

        {
            "description": "Todo 3"
        }
    ])



if __name__ == "__main__":
    app.debug = True
    app.run("0.0.0.0", port=3000)
