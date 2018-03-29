from program_note import app, forms, nav
from flask import render_template

@app.route("/")
def index():
    return render_template('home.html', page_title = "Program Notes")

@app.route("/about")
def about():
    return render_template('about.html', page_title="About Program Notes", no_bg = True)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = forms.RegisterForm()
    if form.validate_on_submit():
        return "Horaay"
    return render_template('signup.html', page_title="Sign Up For Program Notes", form = form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        return "Horaay"
    return render_template('login.html', page_title="Log In", form = form)


