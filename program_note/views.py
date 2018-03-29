from program_note import app
from flask import render_template
from flask_nav import Nav
from flask_nav.elements import Navbar, View

nav = Nav(app)

nav.register_element('navbar', Navbar(
    'thenav',
    View('Home Page', 'index'),
    View('About', 'about'),
    View('Create Account', 'signup'),
    View('Log In', 'login')
))

@app.route("/")
def index():
    return render_template('home.html', page_title = "Program Notes")

@app.route("/about")
def about():
    return render_template('about.html', page_title="About Program Notes", no_bg = True)

@app.route("/signup")
def signup():
    return render_template('signup.html', page_title="Sign Up For Program Notes")

@app.route("/login")
def login():
    return render_template('login.html', page_title="Log In")


