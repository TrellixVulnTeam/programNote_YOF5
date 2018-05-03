from program_note import app, forms, nav, current_user, login_user, login_required, logout_user, new_user, load_user
from flask import render_template, redirect, url_for

@app.route("/")
def index():
    return render_template('home.html', page_title = "Program Notes")

@app.route("/about")
def about():
    return render_template('about.html', page_title="About Program Notes", no_bg = True)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = forms.RegisterForm()
    if form.validate_on_submit():
        if new_user.create_user(form.username.data, form.firstName.data, form.lastName.data, form.email.data, form.pword.data):
            return render_template('loginSignupResult.html', page_title = "Success", msg = "New User Created Successfully")
        else:
            return render_template('loginSignupResult.html', page_title = "Fail", msg = "Username already taken")
    return render_template('signup.html', page_title="Sign Up For Program Notes", form = form)

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = forms.LoginForm()
    if form.validate_on_submit():
        # gets list returned from login function
        status = load_user.login(form.uname.data, form.pword.data)
        # if first item is true, user is logged in and redirected to dashboard
        if status[0] == True:
            login_user(status[1])
            return redirect(url_for('dashboard'))
        # if first item is false, warning message is displayed
        else:
            return render_template("loginSignupResult.html", page_title = 'Fail', msg="Incorrect credentials")
    return render_template('login.html', page_title="Log In", form = form)


@app.route('/dashboard', methods=["GET", "POST"])
@login_required
def dashboard():
    form = forms.AddNoteForm()
    if form.validate_on_submit():
        return form.title.data
    else:
        return render_template('add_note.html', page_title="Welcome", username = current_user.uname, form = form)
    return render_template('add_note.html', page_title = "Welcome", username = current_user.uname, form = form)

@app.route('/allnotes', methods=["GET", "POST"])
@login_required
def allNotes():
    return "All notes"

@app.route('/categories', methods=["GET", "POST"])
@login_required
def categories():
    return "Categories"

@app.route('/account', methods=["GET", "POST"])
@login_required
def accountSettings():
    return "Account settings"

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))