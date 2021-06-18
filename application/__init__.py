import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

SECRET_KEY = os.urandom(32)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bank_branches.db'
db = SQLAlchemy(app)

from application import routes
