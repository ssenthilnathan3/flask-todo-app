from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)



class TODO(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    completed = db.Column(db.Boolean)


@app.route("/")
def index():
    todo_lists = TODO.query.all()
    return render_template("index.html", todo_lists=todo_lists)

if __name__ == '__main__':
    db.create_all()

    new_todo = TODO(title="todo 1", completed=False)
    db.session.add(new_todo)
    db.session.commit()

    app.run(debug=True, port=8080)