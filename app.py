"""Blogly application."""

from crypt import methods
from distutils.log import debug
from flask import Flask, redirect, render_template, request
from importlib_metadata import re
from models import db, connect_db, Blogly
from flask_debugtoolbar import DebugToolbarExtension
from secret import secret_key

# Below this will initiate my Flask app and sets up the configuration to the Database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = secret_key

# DEBUG TOOL BELOW
#       |
#       V
# --------------------------------------------
# debug = DebugToolbarExtension(app)
# --------------------------------------------

# This will connect to the database.
connect_db(app)

# For now the home route redirects to the users page.
@app.route('/')
def homepage():
  return redirect('/users')

# The '/users' route will display all the users that are in the database. 
@app.route('/users')
def users_page():
  users = Blogly.query.all()
  return render_template('users.html', users=users)

# The '/users/new' route will take you to a page to create a new user. 
@app.route('/users/new')
def new_user():
  return render_template('add_users.html')

# The POST version of the 'users/new' route will push the new user to the database. It will then redirect to users. 
@app.route('/users/new', methods=['POST'])
def create_new_user():
  first_name = request.form['first']
  last_name = request.form['last']
  image_url = request.form['image']

  new_user = Blogly(first_name=first_name, last_name=last_name, image_url=image_url)

  db.session.add(new_user)
  db.session.commit()

  return redirect('/users')


# In the '/users/<int>' route <int> will stand for the ID of the user you want to view more information about. 
# Using that ID we are able to query all the data needed to display the profile page. 
@app.route('/users/<int>')
def see_user(int):
  user = Blogly.query.get(int)
  return render_template('profile.html', user=user)

# In the '/users/<int>/edit' route once again the <int> refers to the the user ID. This then be used to fill out the form with the
# current inforamtion. Then you will be allowed to make ammendments to database. 
@app.route('/users/<int>/edit')
def edit_user(int):
  user = Blogly.query.get(int)
  return render_template('edit_user.html', user=user)

# When you submit those ammendments they will be submitted via POST to the '/users/<int>/edit'. 
# This will then actually save those new changes to the database.
@app.route('/users/<int>/edit', methods=['POST'])
def post_edit_user(int):
  user = Blogly.query.get(int)
  first_name = request.form['first']
  last_name = request.form['last']
  image_url = request.form['image']

  user.first_name = first_name
  user.last_name = last_name
  user.image_url = image_url
  db.session.commit()

  return redirect(f'/users/{int}')

# This route will is a POST request that will delete the selcted user. 
@app.route('/users/<int>/delete', methods=['POST'])
def delete_user(int):
  Blogly.query.filter_by(id=int).delete()
  db.session.commit()

  return redirect('/users')