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
    notes = db.relationship('Notes', backref='user', lazy=True)

class Notes(db.Model):
    __tablename__ = "tblNotes"
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.String(20), nullable=False)
    note = db.Column('note', db.String(100), nullable=False)
    category = db.Column('category', db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('tblUser.id'), nullable=False)
