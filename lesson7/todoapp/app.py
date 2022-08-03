from crypt import methods
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:abc@localhost:5432/todoapp"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(), nullable=False)

    def __rep__(self):
        return f"<ID: {self.id}, description {self.description}>"


db.create_all()

@app.route("/")
def index():
    return render_template("index.html", data = Todo.query.all()

        )

@app.route('/todos/create', methods=['POST'])
def create_Todo():
    description = request.form.get('description')
    todo = Todo(description=description)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.debug = True
    app.run("0.0.0.0", port=3000)