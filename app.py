"""Blogly application."""

from crypt import methods
from distutils.log import debug
from unicodedata import name
from flask import Flask, redirect, render_template, request, session
from importlib_metadata import re
from models import db, connect_db, Blogly, Posts, Tags, PostTag
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

@app.route('/')
def homepage():
  '''this will redirect to the homepage where all the posts are displayed (newest is showing first)'''
  posts = Posts.query.order_by(Posts.id.desc()).all()

  return render_template('/homepage.html', posts=posts)


@app.route('/users')
def users_page():
  '''The '/users' route will display all the users that are in the database. '''
  users = Blogly.query.all()
  return render_template('users.html', users=users)


@app.route('/users/new')
def new_user():
  '''The '/users/new' route will take you to a page to create a new user. '''
  return render_template('add_users.html')


@app.route('/users/new', methods=['POST'])
def create_new_user():
  '''The POST version of the 'users/new' route will push the new user to the database. It will then redirect to users. '''
  first_name = request.form['first']
  last_name = request.form['last']
  image_url = request.form['image']

  new_user = Blogly(first_name=first_name, last_name=last_name, image_url=image_url)

  db.session.add(new_user)
  db.session.commit()

  return redirect('/users')



@app.route('/users/<int>')
def see_user(int):
  '''
  In the '/users/<int>' route <int> will stand for the ID of the user you want to view more information about. 
  Using that ID we are able to query all the data needed to display the profile page. 
  '''
  user = Blogly.query.get(int)
  post = Posts.query.order_by(Posts.id.desc()).filter_by(user_id=int)
  return render_template('profile.html', user=user, post=post)


@app.route('/users/<int>/edit')
def edit_user(int):
  '''
  In the '/users/<int>/edit' route once again the <int> refers to the the user ID. This then be used to fill out the form with the
  current inforamtion. Then you will be allowed to make ammendments to database. 
  '''
  user = Blogly.query.get(int)
  return render_template('edit_user.html', user=user)


@app.route('/users/<int>/edit', methods=['POST'])
def post_edit_user(int):
  '''
  When you submit those ammendments they will be submitted via POST to the '/users/<int>/edit'. 
  This will then actually save those new changes to the database.
  '''
  user = Blogly.query.get(int)
  first_name = request.form['first']
  last_name = request.form['last']
  image_url = request.form['image']

  user.first_name = first_name
  user.last_name = last_name
  user.image_url = image_url
  db.session.commit()

  return redirect(f'/users/{int}')


@app.route('/users/<int>/delete', methods=['POST'])
def delete_user(int):
  '''This route will is a POST request that will delete the selcted user. '''
  Blogly.query.filter_by(id=int).delete()
  db.session.commit()

  return redirect('/users')


@app.route('/users/<user_int>/post/new')
def new_post(user_int):
  tags = Tags.query.all()
  '''This will display the form to create a new post'''
  return render_template('new_post.html', tags=tags)
  

@app.route('/users/<user_int>/post/new', methods=['POST'])
def new_post_submit(user_int):
  '''This will submit the new post that was input into the form and ammend it to the database'''
  title = request.form['title']
  content = request.form['content']
  tags = request.form.getlist('tags')
  new_post = Posts(title=title, content=content, user_id=user_int)
  db.session.add(new_post)
  db.session.commit()

  for tag in tags:
    db.session.add(PostTag(post_id=new_post.id, tags_id=tag))
    
  db.session.commit()

  return redirect(f'/users/{user_int}')


@app.route('/posts/<post_int>')
def see_post(post_int):
  '''This will that ONE specific post based on the post ID.'''
  post = Posts.query.get(post_int)
  return render_template('user_post.html', post=post)


@app.route('/posts/<post_int>/edit')
def edit_post(post_int):
  '''This will allow you to edit a post. It will render a form with the current information already loaded in there.'''
  post = Posts.query.get(post_int)
  tags = Tags.query.all()
  return render_template('user_post_edit.html', post=post, tags=tags)


@app.route('/posts/<post_int>/edit', methods=['POST'])
def submit_post_edit(post_int):
  '''This will submit the ammended post to be updated in the database.'''
  post = Posts.query.get(post_int)
  title = request.form['title']
  content = request.form['content']
  tags = request.form.getlist('tags')
  post.title = title
  post.content = content

  PostTag.query.filter_by(post_id = post_int).delete()

  for tag in tags:
     db.session.add(PostTag(post_id=post_int, tags_id=tag))

  db.session.commit()

  return redirect(f'/posts/{post_int}')


@app.route('/posts/<post_int>/delete', methods=['POST'])
def delete_post(post_int):
  '''This will delete the post and then redirect you to that users posts. '''
  PostTag.query.filter_by(post_id = post_int).delete()
  Posts.query.filter_by(id = post_int).delete()
  db.session.commit()

  user = request.form['data']

  return redirect(f'/users/{user}')


@app.route('/tags')
def tags():
  '''This will get all the tags that are in the tags table and display them.'''
  tags = Tags.query.all()
  return render_template('tags.html', tags=tags)

@app.route('/tags/<tag_id>')
def tag_posts(tag_id): 
  '''This will show the posts that are linked to that individual tag'''
  tag = Tags.query.get(tag_id)
  posts = tag.post
  
  return render_template('tag_posts.html', posts=posts, tag=tag)

@app.route('/tags/new')
def new_tags():
  '''This will take you to a form to create new tags'''
  return render_template('new_tag.html')

@app.route('/tags/new', methods=['POST'])
def new_tags_post():
  '''This will take you to a form to create new tags'''
  tag_name = request.form['name']
  new_tag = Tags(name=tag_name)

  db.session.add(new_tag)
  db.session.commit()

  return redirect('/tags')

@app.route('/tags/<tag_id>/edit')
def edit_tag(tag_id):
  '''This will open a form to edit the tag'''
  tag = Tags.query.get(tag_id)

  return render_template('edit_tag.html', tag=tag)

@app.route('/tags/<tag_id>/edit', methods=['POST'])
def edit_tag_post(tag_id):
  '''This will open a form to edit the tag'''
  tag = Tags.query.get(tag_id)
  name = request.form['name']
  tag.name = name
  db.session.commit()

  return redirect(f'/tags/{tag.id}')

@app.route('/tags/<tag_id>/delete', methods=['POST'])
def delete_tag(tag_id):
  '''This route will is a POST request that will delete the selcted user. '''
  PostTag.query.filter_by(tags_id = tag_id).delete()
  Tags.query.filter_by(id=tag_id).delete()
  db.session.commit()

  return redirect('/tags')
