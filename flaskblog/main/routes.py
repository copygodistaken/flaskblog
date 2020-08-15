from flask import Blueprint, render_template, request
from flaskblog.models import Post

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    # title = "Welcome"
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=10)
    return render_template('home.html', posts=posts)

@main.route("/about")
def about():
    text1 = '''The SimpsonStuff Blog is basically just a way for the Simpson's (and friends and pets) can communicate with each other about the goings-on of their lives.'''
    text2 = '''In the sidebar to the right, you'll see links to a few other pages the Simpson's have for their Frogs, Dogs, Notes and other stuff.  Perhaps more will be added in the future. This is a development server for Eric, so keep in mind that it might disappear at any moment, or have additions or modifications to the look, feel, and even the function of the blog and associated websites.'''
    return render_template('about.html', text1=text1, text2=text2)
