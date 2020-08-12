from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post


posts = [
    {
        'author': 'Eric',
        'title': 'Blog Post One',
        'content': 'First post content',
        'date_posted': 'April 20, 2020'
    },
    {
        'author': 'Juli',
        'title': 'Blog Post Two',
        'content': 'Second post content',
        'date_posted': 'April 21, 2020'
    }

]

@app.route("/")
@app.route("/home")
def home():
    title="Welcome"
    return render_template('home.html', posts=posts, title=title)
    print(posts)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Log in unsuccessful, please check your password and username.', 'danger')
    return render_template('login.html', title='Log In', form=form)
