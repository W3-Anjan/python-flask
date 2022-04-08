
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

mapp = Flask(__name__) # the main module
# set a config variable for the name and the path of the database
# mysql: https://medium.com/@manutsssav/flask-api-with-jwt-authentication-cc1851c7d36f
mapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite' 
# 
mapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# create the database 
db = SQLAlchemy(mapp)

# create a database model
class Todo(db.Model): # inherit the db.Model
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


@mapp.route('/') # decorator
def index():
    # show all todos
    todo_list = Todo.query.all()
    print(todo_list)
    return render_template('base.html', todo_list=todo_list)

@mapp.route("/add", methods=['POST'])
def add():
    # add new item
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))


@mapp.route("/update/<int:todo_id>")
def update(todo_id):
    # update item
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("index"))    


@mapp.route("/delete/<int:todo_id>")
def delete(todo_id):
    # update item
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))  

if __name__== "__main__":

    # create our database here
    db.create_all()
    
    mapp.run(debug=True)    
