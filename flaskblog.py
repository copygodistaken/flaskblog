from flask import Flask, render_template, url_for, flash, redirect
app = Flask(__name__)
from forms import RegistrationForm, LoginForm

app.config['SECRET_KEY'] = "1856f68722d2489a636366b812c22c1a"

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


if __name__ == '__main__':
    app.run(debug=True)

