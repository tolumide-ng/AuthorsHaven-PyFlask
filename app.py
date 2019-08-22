from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://' + \
    os.path.join(basedir, 'db.postgres')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)


class User (db.Model):
    id = db.Column(db.integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    admin = db.Column(db.Boolean)
    active = db.Column(db.Boolean)

    def __init__(self, public_id, username, email, admin, active):
        self.public_id = public_id
        self.username = username
        self.email = email
        self.admin = admin
        self.active = active


# # User schema
# class UserSchema(ma.Schema):
#     class Meta:
#         fields = ('public_id', 'username', 'email', 'admin', 'active')


# # Init schema
# user_schema = UserSchema(strict=True)


class Article (db.Model):
    id = db.Column(db.integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(200))
    content = db.Column(db.String(1000))
    authorId = db.Column(db.Integer)

    def __init__(self, title, description, content, authorId):
        self.title = title
        self.description = description
        self.content = content
        self.authorId = authorId

# # User schema


# class ArticleSchema(ma.Schema):
#     class Meta:
#         fields = ('title', 'description', 'content', 'authorId')


# # Init schema
# user_schema = UserSchema(strict=True)


class Follows (db.Model):
    id = db.Column(db.integer, primary_key=True)
    followedId = db.Column(db.integer)
    followeeId = db.Column(db.integer)

    def __init__(self, followedId, followeeId):
        self.followedId = followedId
        self.followeeId = followeeId


    # Run Server
if __name__ == '__main__':
    app.run(debug=True)
