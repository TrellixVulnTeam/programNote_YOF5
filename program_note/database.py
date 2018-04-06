from flask_sqlalchemy import SQLAlchemy
from program_note import app
from flask_login import UserMixin

db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    __tablename__ = 'tblUser'
    id = db.Column('id', db.Integer, primary_key=True)
    uname = db.Column('uname', db.String(18), unique=True)
    fname = db.Column('fname', db.Unicode, nullable=False)
    lname = db.Column('lname', db.Unicode)
    email = db.Column('email', db.Unicode, nullable=False)
    pword = db.Column('pword', db.String(80), nullable=False)