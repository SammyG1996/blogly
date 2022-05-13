"""Models for Blogly."""

from turtle import title
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# This is a method that you will be able to call in the app.py file. It will allow you to initiate the connction to the database.
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

# This will contain the schema and the different methods pertaining to the Blogly table.
class Blogly(db.Model):
    '''Blog Users'''
    __tablename__ = 'blogly'

    id = db.Column(db.Integer, 
                  primary_key=True, 
                  autoincrement=True)

    first_name = db.Column(db.String(), 
                          nullable=False)

    last_name = db.Column(db.String(), 
                          nullable=False)
                          
    image_url = db.Column(db.String(), 
                          nullable=True)


class Posts(db.Model):
    '''This table will contain the posts'''

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    title = db.Column(db.String(), nullable=False)

    content = db.Column(db.String(), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.now())

    user_id = db.Column(db.Integer, db.ForeignKey('blogly.id'))

    # Relationship With the Blogly database
    user = db.relationship('Blogly', backref='post')
